from django.conf.urls import url
from django.contrib import admin
from howto import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^world/$', views.world, name='world'),
    url(r'^admin/', admin.site.urls),
]
