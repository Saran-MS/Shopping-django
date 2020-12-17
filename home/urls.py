from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('shops',views.shops,name='shops'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('checkout/<int:id>', views.checkout, name='checkout'),
    path('checkout/add/<int:id>', views.add, name='add'),
    path('cart', views.cart, name='cart'),
]