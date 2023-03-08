from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        #image => imagefile
        model = Photo
        fields = ('title', 'autho', 'imagefile',
                  'description', 'price')
