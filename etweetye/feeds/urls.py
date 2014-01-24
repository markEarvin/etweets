from django.conf.urls import patterns, url

from feeds import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)