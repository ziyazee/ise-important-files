
from django.conf.urls import url,include
from django.contrib import admin
from letsdoit import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home,name='home'),
    url(r'^index/',views.index,name='index'),
    url(r'^testing/',views.testing,name='testing'),
# url(r'logout/$',views.logout_view,name="logout"),
    url(r'^(?P<year>[\f\w-]+)/$',views.subjects,name='subjects'),
    url(r'^files/(?P<categorie>[\f\w-]+)/$',views.files,name='files'),
    url(r'',include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
