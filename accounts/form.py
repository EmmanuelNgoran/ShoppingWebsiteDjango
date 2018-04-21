from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from shoppingBoard.models import UserData

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    # phoneNumber=forms.IntegerField( help_text='ex: 5555555555', widget=forms.TextInput(attrs={ 'max_length': 10, 'required': True, } ), )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class UserData
class UserDataForm(ModelForm):
    class Meta:
        model=UserData
        fields=('address','phone_number')
        