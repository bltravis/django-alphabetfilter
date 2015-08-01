from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.shortcuts import _get_queryset

class ActiveAlphabet(models.Model):
    site = models.ForeignKey(Site)
    content_type = models.ForeignKey(ContentType)
    content_type_field = models.CharField(max_length=25)
    active_alphabet = models.CharField(max_length=1000, blank=True, default=u'')
    
    def __unicode__(self):
        return u'Active alphabet for %s on %s' % (self.content_type, self.site)
    
    class Meta:
        unique_together = (('site', 'content_type', 'content_type_field'),)


# Signal handler to update active alphabet for a given model
## TODO: Use model introspection to determine name for Site foreignkey
def alpha_check(sender, **kwargs):
    instance = kwargs['instance']
    active_alphabets = ActiveAlphabet.objects.filter(site=Site.objects.get_current(), content_type=ContentType.objects.get_for_model(sender))
    if active_alphabets:
        for active_alphabet in active_alphabets:
            for field_name in sender.alphafilter_on:
                if field_name == active_alphabet.content_type_field:
                    active = active_alphabet.active_alphabet
                    first_letter = instance._meta.get_field(field_name).value_from_object(instance).split()[-1][0].upper()
                    if not first_letter in active:
                        new_active = active + first_letter
                        _new_active = list(new_active)
                        _new_active.sort()
                        new_active = ''.join(_new_active)
                        active_alphabet.active_alphabet = new_active
                        active_alphabet.save()
    else:
        for field_name in sender.alphafilter_on:
            active_alphabet = ActiveAlphabet(site=Site.objects.get_current(), content_type=ContentType.objects.get_for_model(sender), content_type_field=field_name, active_alphabet=u'%s' % (instance._meta.get_field(field_name).split()[-1][0].upper(),))
            active_alphabet.save()

def alpha_clean(sender, **kwargs):
    instance = kwargs['instance']
    active_alphabets = ActiveAlphabet.objects.filter(site=Site.objects.get_current(), content_type=ContentType.objects.get_for_model(sender))
    if active_alphabets:
        for active_alphabet in active_alphabets:
            for field_name in sender.alphafilter_on:
                if field_name == active_alphabet.content_type_field:
                    active = active_alphabet.active_alphabet
                    first_letter = instance._meta.get_field(field_name).value_from_object(instance).split()[-1][0].upper()
                    if first_letter in active:
                        still_active = sender.objects.filter(client__site=Site.objects.get_current(), **{'%s__istartswith' % field_name: first_letter})
                        if still_active:
                            return ''
                        else:
                            old_active = list(active)
                            old_active.remove(first_letter)
                            new_active = ''.join(old_active)
                            active_alphabet.active_alphabet = new_active
                            active_alphabet.save()

                        