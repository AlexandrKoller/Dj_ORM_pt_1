from django.contrib import admin
from phones.models import Phone


# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'release_date']
    prepopulated_field = {'slug': ('name',)}

