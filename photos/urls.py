from django.conf.urls import patterns, url

from photos import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='photos')
    )