from django.shortcuts import render,redirect
from django.views import View
from .forms import UserLoginForm,UserRegistrationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import random


class UserLoginView(View):
   form_class = UserLoginForm

   def get(self,request):
       return render(request,'accounts/login.html',{'form':self.form_class})

   def post(self,request):
       form=self.form_class(request.POST)
       if form.is_valid():
           cd=form.cleaned_data
           user=authenticate(username=cd['username'],password=cd['password'])
           if user:
               login(request,user)
               messages.success(request,'شما با موفقیت وارد شده اید.','success')
               return redirect('shop:workshop')
           messages.error(request,'نام کاربری یا کلمه عبور اشتباه می باشد.','error')
           return render(request,'accounts/login.html',{'form':form})



class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'شما با موفقیت از حساب خود خارج شده اید.','success')
        return redirect('shop:home')



class UserRegisterView(View):
    class_form=UserRegistrationForm
    def get(self,request):
        return render(request,'accounts/registration.html',{'form':self.class_form})

    def post(self):
        pass
