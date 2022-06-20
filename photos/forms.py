from django.core.exceptions import ValidationError

from photos.models import Photo
from django.forms import ModelForm


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['owner']


