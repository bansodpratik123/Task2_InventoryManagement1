from django.urls import path
from .views import signupView, loginView, logoutView

urlpatterns=[
    path('register/',signupView, name='register'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView, name='logout'),

]