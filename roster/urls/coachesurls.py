from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('', 
        url(r'^$', views.CoachView, name='coaches'),
    )

