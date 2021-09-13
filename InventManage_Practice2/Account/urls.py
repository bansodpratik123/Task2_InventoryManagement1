from django.urls import path
from .views import loginView, signUpView, logoutView

urlpatterns=[
    path('signup/',signUpView, name='signup'),
    path('login/', loginView, name='login'),
    path('logout/', logoutView, name='logout'),

]