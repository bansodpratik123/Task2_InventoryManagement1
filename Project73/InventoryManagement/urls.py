from django.urls import path
from .views import addProductView, showProductView, homepageView, updateProductView, deleteProductView

urlpatterns=[
    path('home/', homepageView, name='homepage'),
    path('add-product/', addProductView, name='addproduct'),
    path('show-product/', showProductView, name='showproduct'),
    path('update-product/<int:id_fe>/', updateProductView, name='updateproduct'),
    path('delete-product/<int:id_fe>/', deleteProductView, name='deleteproduct'),
]