from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.forms import fields, widgets,DateTimeField
from django.utils.translation import ugettext_lazy as _
from .models import Post,Contect

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
                    }


class LoginForm(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label =_("Password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc','written_by']
        labels = {'title':'Title','desc':'Description','post_date':'Post Date'}
        widgets ={'title':forms.TextInput(attrs={'class':'form-control'}),
                  'desc':forms.Textarea(attrs={'class':'form-control'}),
                  'written_by':forms.TextInput(attrs={'class':'form-control'}),
                }

class ContectForm(forms.ModelForm):
    class Meta:
        model = Contect
        fields = ['name','email','mobile','address','message']
        labels = {'name':'Name','email':'Email','address':'Address','messagae':'Message'}
        widgets ={'name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
                  'mobile':forms.NumberInput(attrs={'class':'form-control'}),
                  'address':forms.TextInput(attrs={'class':'form-control'}),
                  'message':forms.Textarea(attrs={'class':'form-control'}),
                }