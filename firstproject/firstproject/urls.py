
from django.conf.urls import url
from django.contrib import admin

from letsdoit import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^letsdoit/(\d+)/',views.myinfo_detail,name='myinfo_detail'),


]
