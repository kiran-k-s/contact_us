from django import forms

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
