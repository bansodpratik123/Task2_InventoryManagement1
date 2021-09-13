from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def signupView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.method)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='Account/SignupForm.html'
    context={'form':form}
    return render(request, template_name, context)

def loginView(request):
    if request.method=='POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        user=authenticate(username=u, password=p)
        if user is not None:
            login(request,user)
            redirect('showproduct')
        else:
            messages.error(request, 'Invalid Credentials')
    template_name='Account/LoginForm.html'
    context={}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('home')
