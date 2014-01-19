from django.shortcuts import render
from django.views.generic import TemplateView
        
class PhotoView(TemplateView):
    template_name = "under_construction.html"
    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        return context
        
class ResourceView(TemplateView):
    template_name = "under_construction.html"
    def get_context_data(self, **kwargs):
        context = super(ResourceView, self).get_context_data(**kwargs)
        return context
        
class CoachView(TemplateView):
    template_name = "under_construction.html"
    def get_context_data(self, **kwargs):
        context = super(CoachView, self).get_context_data(**kwargs)
        return context