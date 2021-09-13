from django.urls import path
from .views import signupView,loginView,logoutView
urlpatterns=[
    path('signup/',signupView, name='signup'),
    path('login/', loginView, name='login'),
    path('signup/', logoutView, name='logout'),

]