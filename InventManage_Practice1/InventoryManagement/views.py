from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepageView(request):
    template_name='InventoryManagement/Homepage.html'
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
    template_name='InventoryManagement/AddProduct.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='login')
def showProductView(request):
    records=Products.objects.all()
    template_name='InventoryManagement/ShowProduct.html'
    context={'records':records}
    return render(request,template_name,context)

def updateProductView(request,id_fe):
    record=Products.objects.get(id=id_fe)
    form=ProductModelForm(instance=record)
    if request.method=='POST':
        form=ProductModelForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='InventoryManagement/UpdateProduct.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteProductView(request,id_fe):
    record=Products.objects.get(id=id_fe)
    record.delete()
    return redirect('showproduct')