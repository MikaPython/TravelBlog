from django.contrib import admin
from main.models import *

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 10

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin, ]


admin.site.register(Category)


