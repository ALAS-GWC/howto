from django.conf.urls import url
from django.contrib import admin
from howto import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^world/$', views.world, name='world'),
    url(r'^algebra1/$', views.algebra1, name='algebra1'),
    url(r'^algebra2-trig/$', views.algebra2trig, name='algebra2trig'),
    url(r'^apbio/$', views.apbio, name='apbio'),
    url(r'^apecon/$', views.apecon, name='apecon'),
    url(r'^apgov/$', views.apgov, name='apgov'),
    url(r'^apphysics/$', views.apphysics, name='apphysics'),
    url(r'^apush/$', views.apush, name='apush'),
    url(r'^BC/$', views.BC, name='BC'),
    url(r'^bio/$', views.bio, name='bio'),
    url(r'^chem/$', views.chem, name='chem'),
    url(r'^comp/$', views.comp, name='comp'),
    url(r'^euro/$', views.euro, name='euro'),
    url(r'^geometry/$', views.geometry, name='geometry'),
    url(r'^lit/$', views.lit, name='lit'),
    url(r'^physics/$', views.physics, name='physics'),
    url(r'^precalc/$', views.precalc, name='precalc'),
    url(r'^english/$', views.english, name='english'),
    url(r'^history/$', views.history, name='history'),
    url(r'^math/$', views.math, name='math'),
    url(r'^science/$', views.science, name='science'),
    url(r'^college/$', views.college, name='college'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
]
