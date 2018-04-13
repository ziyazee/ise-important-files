from django import forms


from .models import filest

class PostForm(forms.ModelForm):
    # def get_absolute_url():
    #     return "/files/%s"
    # categorie=get_absolute_url()
    # def details(request,name):
    #     category=filest.objects.get(categorie=name)   
    class Meta:
        # category=clasyear.objectsTextField().get(categorie=name)

        #here i need to assign categorie value from url parameter
        #categorie=**something**
        
        model = filest
        fields = ('fname','fdescription', 'categorie')
        widgets = {'categorie': forms.HiddenInput()}
        