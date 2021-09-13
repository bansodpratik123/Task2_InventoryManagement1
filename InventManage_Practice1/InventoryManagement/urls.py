from django.urls import path
from .views import homepageView, addProductView, showProductView, updateProductView, deleteProductView

urlpatterns=[
    path('home/',homepageView, name='home'),
    path('addproduct/',addProductView, name='addproduct'),
    path('showproduct/', showProductView, name='showproduct'),
    path('updateproduct/<int:id_fe>', updateProductView, name='updateproduct'),
    path('deleteproduct/<int:id_fe>', deleteProductView, name='deleteproduct'),

]