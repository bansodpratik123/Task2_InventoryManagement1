from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def signupView(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='Accounts/SignupForm.html'
    context={'form':form}
    return render(request,template_name,context)

def loginView(request):
    if request.method == 'POST':
        u=request.POST.get('un')
        p=request.POST.get('pw')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('addproduct')
        else:
            messages.error(request,'Credential Invalid')
    template_name='Accounts/LoginForm.html'
    context={}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')