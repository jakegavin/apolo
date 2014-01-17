from django.shortcuts import render
from photos.models import Group, Image

def index(request):
    groups = Group.objects.all()
    images = Image.objects.all()
    context = {'groups': groups, 'images': images}
    return render(request, 'photos/index.html', context)
    