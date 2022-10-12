from django.contrib import admin

from apps.core.models import Brand, Car, Color

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Car)
