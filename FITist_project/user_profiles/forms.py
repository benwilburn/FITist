from django import forms
# from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
                    label="Username", max_length=30,
                    widget=forms.TextInput(
                        attrs={'class': 'form-control',
                               'name': 'username'}
                        )
                    )
    password = forms.CharField(
                    label="Password", max_length=30,
                    widget=forms.PasswordInput(
                        attrs={'class': 'form-control', 'name': 'password'}
                        )
                    )


class UserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    confirm_email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'password',
            'confirm_password',
        ]

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password fields do not match"
            )

        if email != confirm_email:
            raise forms.ValidationError(
                "email and confirm_email fields do not match"
            )
