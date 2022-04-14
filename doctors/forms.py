from django import forms
from.models import Doctor



class PostForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=('__all__')