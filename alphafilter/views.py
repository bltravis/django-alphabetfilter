"""
A generic view for filtering querysets via alphafilter
"""
from __future__ import unicode_literals
from django.shortcuts import render
# from django.template import RequestContext

def alphafilter(request, queryset, template):
    """
    Render the template with the filtered queryset
    """

    qs_filter = {}
    for key in request.GET.keys():
        if '__istartswith' in key:
            qs_filter[str(key)] = request.GET[key]
            break

    return render(
        request,
        template,
        {'objects': queryset.filter(**qs_filter)}
    )
