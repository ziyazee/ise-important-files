from django import forms


from .models import filest    

from .models import clasyear
class PostForm(forms.ModelForm):
    class Meta:   
        fdescription = forms.CharField( widget=forms.Textarea() )
        model = filest
        fields = ('fname','fdescription','usn' ,'categorie',)
        widgets = {'categorie': forms.HiddenInput(),'usn': forms.HiddenInput()}
        