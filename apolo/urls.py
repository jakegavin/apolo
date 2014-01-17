from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from common.views import CoachView, ScheduleView, PhotoView, ResourceView

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apolo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^$', include('roster.urls')),
    url(r'^roster/', include('roster.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coaches/', CoachView.as_view(), name='coaching_staff'),
    url(r'^schedule/', ScheduleView.as_view(), name='schedule'),
    url(r'^photos/', include('photos.urls')),
    url(r'^resources/', ResourceView.as_view(), name='resources'),
    url(r'^coaching_staff/', CoachView.as_view(), name='coaching_staff'),
    url(r'^alumni/', TemplateView.as_view(template_name="under_construction.html")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
