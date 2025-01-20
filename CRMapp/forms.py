
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

# the registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = {'username', 'email' , 'password1' , 'password2'}


class AddRecordForm(forms.ModelForm):
    full_name = forms.CharField(required=True , widget=forms.widgets.TextInput(attrs={"placeholder": "full name"}))
    email = forms.EmailField(required=True , widget=forms.widgets.TextInput(attrs={"placeholder": "email"}))
    phone = forms.CharField(required=True , widget=forms.widgets.TextInput(attrs={"placeholder": "phone"}))
    adresse = forms.CharField(required=True , widget=forms.widgets.TextInput(attrs={"placeholder": "adresse"}))
    class Meta:
        model = Customer
        exclude = ('user',)