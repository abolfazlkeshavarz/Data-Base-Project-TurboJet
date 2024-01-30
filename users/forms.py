from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email','username','first_name','last_name', 'phone_number', 'national_id', 'address', 'birth_date', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'email'
                }),
            'username': forms.TextInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'Username'
                }),
            'first_name': forms.TextInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'First Name'
                }),
            'last_name':forms.TextInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'Last Name'
                }),
            'birth_date': forms.DateInput(attrs={
                'type': 'date',
                'class': "input-group mb-3 input-group-text w-25",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'id':"basic-addon1",
                'placeholder': 'Birthday'
                }),
            'phone_number': forms.NumberInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'Phone Number'
                }),
            'national_id': forms.NumberInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'National Number'
                }),
            'address':forms.Textarea(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': ' Address'
                }),
            'password1': forms.TextInput(attrs={
                'type':'password',
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'password'
                }),
            'password2': forms.TextInput(attrs={
                'type':'password',
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'password confirm'
                }),
                }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name','last_name', 'phone_number', 'national_id', 'address', 'birth_date')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'Username'
                }),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'id':"basic-addon1",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'Password'
                }))

