from django import forms
from .models import User
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'Username'}))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg','placeholder':'Password'}))


class UserRegistrationForm(forms.ModelForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Password conformation',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('email','phone_number','full_name')


    def clean_email(self):
        cleaned_email=self.cleaned_data.get('email')
        if not cleaned_email:
            raise ValueError('ایمیل معتبر نمی باشد.')
        email_check=User.objects.filter(email=cleaned_email).exists()
        if email_check:
            raise ValidationError('ایمیل قبلا ثبت شده است.')
        return cleaned_email

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords dont match')
        return cd['password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


