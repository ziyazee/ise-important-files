from django.contrib import admin

from .models import clasyear
from .models import filest


@admin.register(filest)
class  Ziya(admin.ModelAdmin):
    list_display=['fname','fdescription','categorie']

   
#admin.site.register(admin,Myinfo)