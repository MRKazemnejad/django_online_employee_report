from django.urls import path
from . import views


app_name='shop'

urlpatterns=[
    path('', views.UserHomeView.as_view(), name='home'),
    path('workshop/', views.ProductView.as_view(), name='workshop'),
    path('product_details/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
    path('cart/',views.CartView.as_view(),name='cart'),
    path('add_cart/<int:product_id>/',views.CartAddView.as_view(),name='add_cart'),
    path('remove_cart/<str:product_id>/',views.CartRemoveView.as_view(),name='remove_cart'),
    path('order_create/',views.OrderCreateView.as_view(),name='order_create'),
    path('order_detail/<int:order_id>/',views.OrderDetailView.as_view(),name='order_detail'),
    path('apply_coupon/<int:order_id>/',views.CouponPriceView.as_view(),name='apply_coupon'),
    path('final_price/<int:order_id>/',views.FinalPriceView.as_view(),name='final_price'),
]