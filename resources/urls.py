from django.conf.urls import patterns, url

from resources import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='resources')
    )