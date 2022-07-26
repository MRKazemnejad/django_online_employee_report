from django.shortcuts import render
from django.views import View

# Create your views here.


class UserHomeView(View):
    def get(self,request):
         return render(request,'shop/index.html')