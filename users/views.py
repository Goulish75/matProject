from django.shortcuts import render,HttpResponseRedirect
from .forms import UserCreateForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
class Users:
    def user_register(self):
        form = UserCreateForm(self.POST or None)
        if form.is_valid():
            new_user = form.save(commit=True)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            yetkili_mi = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if yetkili_mi:
                login(self,new_user)
                return HttpResponseRedirect("/")

        return render(self,"user_register.html",context={"form":form})
    def user_login(self):
        form = LoginForm(self.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(self,user)
                return HttpResponseRedirect("/")
        return render(self,'login.html',context={"form":form})

    def user_cıkısYap(self):
        logout(self)
        return HttpResponseRedirect("/")
    def hesap_degistir(self):
        logout(self)
        return HttpResponseRedirect("girisYap")
