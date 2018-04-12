
from django.conf.urls import url
from django.contrib import admin

from letsdoit import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^index/',views.index,name='index'),
    url(r'^(?P<year>[\f\w-]+)/$',views.subjects,name='subjects'),
    url(r'^details/(?P<name>[\f\w-]+)/$',views.details,name='details'),
    url(r'^details/files/(?P<categorie>[\f\w-]+)/$',views.files,name='files'),



]
