from django.urls import path
from .views import homepageView, addProctView, showProctView, updateProctView, deleleProductView

urlpatterns=[
    path('home/', homepageView, name='home'),
    path('addproduct/', addProctView, name='addproduct'),
    path('showproduct/', showProctView, name='showproduct'),
    path('updateproduct/<int:id_fe>/', updateProctView, name='updateproduct'),
    path('deleteproduct/<int:id_fe>/', deleleProductView, name='deleteproduct'),

]