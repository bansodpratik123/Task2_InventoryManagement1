from django.shortcuts import render,redirect
from .forms import ProductModelForm
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepageView(request):
    template_name='Homepage.html'
    context={}
    return render(request,template_name,context)

@login_required(login_url='login')
def addProductView(request):
    form=ProductModelForm()
    if request.method=='POST':
        form=ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='AddProduct.html'
    context={'form':form}
    return render(request,template_name,context)


def showProductView(request):
    template_name='ShowProduct.html'
    records=Product.objects.all()
    context={'records':records}
    return render(request,template_name,context)

def updateProductView(request,id_fe):
    product=Product.objects.get(id=id_fe)
    form=ProductModelForm(instance=product)
    if request.method=='POST':
        form=ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='AddProduct.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteProductView(request,id_fe):
    product=Product.objects.get(id=id_fe)
    product.delete()
    return redirect('showproduct')