from django.contrib import admin
from .models import Samochody, Marka, Model, Kategoria

# Register your models here.
admin.site.register(Samochody)
admin.site.register(Marka)
admin.site.register(Model)
admin.site.register(Kategoria)