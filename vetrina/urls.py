from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'collezioni/$', views.collezioni, name='collezioni'),
    url(r'eventi/$', views.eventi, name='eventi'),
    url(r'contatti/$', views.contatti, name='contatti'),
    url(r'about/$', views.about, name='about'),
]