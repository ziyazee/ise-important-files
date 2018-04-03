from django.contrib import admin

from .models import title
from .models import Myinfo
from .models import child
from .models import livings
from .models import clasyear


@admin.register(clasyear)
class  Ziya(admin.ModelAdmin):
    list_display=['year','name','description']

   
#admin.site.register(admin,Myinfo)