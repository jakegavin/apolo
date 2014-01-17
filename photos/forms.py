from django import forms as f
from apolo.photos.models import *

def ImageForm(f.ModelForm):
    class Meta:
        model = Image
        exclude = "image width height hidden group thumbnail".split()
        attrs = dict(cols=70)
        widgets = dict( description=f.Textarea(attrs=attrs) )
    
    #not sure if I need the following lines
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(UserModelForm, self).__init__(*args, **kwargs)
    def __iter__(self):
        """Workaround for a bug in modelformset factory."""
        for name in self.fields:
            if name!="id": yield self[name]


def AddImageForm(f.ModelForm):
    class Meta:
        model = Image
        exclude = "width height hidden group thumbnail".split()
        attrs = dict(cols=70, rows=2)
        widgets = dict( description.f.Textarea(attrs=attrs) )