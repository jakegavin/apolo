from django.conf.urls import patterns, url

from schedule import views

urlpatterns = patterns('', 
        url(r'^$', views.ScheduleView, name='schedule'),
    )

