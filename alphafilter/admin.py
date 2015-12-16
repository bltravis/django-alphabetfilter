# from django.db.models import get_model
from __future__ import unicode_literals
from django.apps import apps
from django.contrib import admin
from django.conf import settings

MODEL_REGISTRY = getattr(settings, 'ALPHAFILTER_ADMIN_FIELDS', {})
FIELDS = {}

for key, val in MODEL_REGISTRY.items():
    if isinstance(key, basestring):
        FIELDS[apps.get_model(*key.split('.'))] = val


for model,modeladmin in admin.site._registry.items():
    if model in FIELDS:
        admin.site.unregister(model)
        admin.site.register(model, type('newadmin', (modeladmin.__class__,), {
            'alphabet_filter': FIELDS[model],
        }))
