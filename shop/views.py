from django.shortcuts import render
from django.views import View


class UserHomeView(View):
    def get(self,request):
         return render(request,'shop/index.html')


class UserWorkshopView(View):
    def get(self,request):
        return render(request,'shop/wokshop.html')
