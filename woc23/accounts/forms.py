from django.forms import ModelForm
from .models import Company_Name
# from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post

class Com_Form(ModelForm):
    class Meta:
        model = Company_Name
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control','placeholder':'title'}),
            'author':forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            'body':forms.Textarea(attrs={'class': 'form-control','placeholder':'Start Typing Here'}),
        }
        