from django import forms


from .models import filest

class PostForm(forms.ModelForm):
    class Meta:    
        model = filest
        fields = ('fname','fdescription', 'categorie')
        widgets = {'categorie': forms.HiddenInput()}
        