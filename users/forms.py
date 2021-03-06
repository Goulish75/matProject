from django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UserCreateForm, self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class":"form-control"}
        self.fields['password'].widget = forms.PasswordInput(attrs={"class":"form-control"})
    class Meta:
        model = User
        fields = ["username","first_name","last_name","password"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,required=True,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
