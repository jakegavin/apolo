from django.shortcuts import render
from photos.models import Group, Image

def index(request):
    groups = Group.objects.all()
    images = Image.objects.all()

    def get_group_images(images, ggroup):
        '''Takes a list of images and a group.
        Returns a list of all images in the group.'''
        img_list = []
        for image in images:
            if image.group == ggroup:
                img_list.append(image)
            else:
                pass
        return img_list

    image_sets = []
    for group in groups:
        if group.hidden == False:
            imgs = get_group_images(images, group)
            app = [group, imgs]
            image_sets.append(app)
        if group.hidden == True:
            pass

    context = {'groups': groups, 'images': images, 'image_sets': image_sets}
    return render(request, 'photos/index.html', context)
    