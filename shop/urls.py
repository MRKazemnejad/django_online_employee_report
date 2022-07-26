from django.urls import path
from . import views


app_name='shop'

urlpatterns=[
    path('', views.UserHomeView.as_view(), name='home')
]