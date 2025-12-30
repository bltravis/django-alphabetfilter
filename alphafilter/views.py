"""
A generic view for filtering querysets via alphafilter
"""
from django.shortcuts import render


def alphafilter(request, queryset, template):
    """
    Render the template with the filtered queryset
    """

    qs_filter = {}
    for key in list(request.GET.keys()):
        if '__istartswith' in key:
            qs_filter[key] = request.GET[key]
            break

    return render(
        request,
        template,
        {'objects': queryset.filter(**qs_filter)}
    )
