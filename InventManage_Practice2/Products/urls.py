from django.urls import path
from .views import homepageView, addProductView, showProductView, updateProductView, deleteProductView

urlpatterns=[
    path('home/',homepageView, name='home'),
    path('add-product/', addProductView, name='addproduct'),
    path('show-product/', showProductView, name='showproduct'),
    path('update-product/<int:id_fe>/', updateProductView, name='updateproduct'),
    path('delete-product/<int:id_fe>/', deleteProductView, name='deleteproduct'),

]