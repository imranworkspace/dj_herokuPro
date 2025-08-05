from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(label='Student Name',widget=forms.TextInput(attrs={'placeholder':'enter name'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'enter email'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))
