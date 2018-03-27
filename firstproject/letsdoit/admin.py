from django.contrib import admin

from .models import Myinfo
@admin.register(Myinfo)
class  Ziya(admin.ModelAdmin):
    list_display=['name','age','gender']
