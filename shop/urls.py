from django.urls import path
from . import views


app_name='shop'

urlpatterns=[
    path('', views.UserHomeView.as_view(), name='home'),
    path('workshop/', views.ProductView.as_view(), name='workshop'),
    path('product_details/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
]