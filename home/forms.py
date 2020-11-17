from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactusForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=4, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : 'Name'}))
    email = forms.EmailField(max_length=45 , widget=forms.EmailInput(
        attrs={"class":"form-control", "placeholder":"Email address"}
    ))
    phone = forms.CharField(max_length=10, min_length=10, widget=forms.TextInput(
        attrs={"class":"form-control", "placeholder":"Phone Number"}
    ),required=False)
    description = forms.CharField(min_length=20, widget=forms.Textarea(
        attrs={"class":"form-control" ,"placeholder":"Description"}
    ))

    
    
    
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
    
    
    
class RegisterForm(forms.Form):
        username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
        password_first = forms.CharField(label="inputPassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
        password_again = forms.CharField(label="confirmPassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
        
        def clean(self):
            cleaned_data = self.cleaned_data
            password_one = self.cleaned_data.get('password_first')
            password_two = self.cleaned_data.get('password_again')
            if password_one != password_two:
                raise forms.ValidationError("Passwords dont match")
            return cleaned_data
        
        def clean_username(self):
            username = self.cleaned_data.get('username')
            qs = User.objects.filter(username=username)
            if qs.exists():
                raise forms.ValidationError("The username you have chosen is unavailable")
            return username
        
        def clean_email(self):
            email_address = self.cleaned_data.get('email')
            qs = User.objects.filter(email=email_address)
            if qs.exists():
                raise forms.ValidationError("The email you have chosen is already registered")
            return email_address
        
        
            