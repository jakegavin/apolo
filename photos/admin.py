from django.contrib import admin
from photos.models import Group, Image

class GroupAdmin(admin.ModelAdmin):
    list_display = ["title", "image_links"]
    
admin.site.register(Group, GroupAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_dislpay = "__unicode__ title group created".split()

admin.site.register(Image, ImageAdmin)