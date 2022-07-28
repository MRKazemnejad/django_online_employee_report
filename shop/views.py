from django.shortcuts import render
from django.views import View
from .models import Product,Category


class UserHomeView(View):
    def get(self,request):
         product=Product.objects.all()
         return render(request,'shop/index.html',{'products':product})


class UserWorkshopView(View):
    def get(self,request):
        return render(request,'shop/wokshop.html')
