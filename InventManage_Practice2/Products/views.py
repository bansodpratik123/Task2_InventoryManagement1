from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductsModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepageView(request):
    template_name='Products/Homepage.html'
    context={}
    return render(request,template_name, context)

@login_required(login_url='login')
def addProductView(request):
    form=ProductsModelForm()
    if request.method=='POST':
        form=ProductsModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showproduct')

    template_name='Products/AddProduct.html'
    context={'form':form}
    return render(request,template_name, context)

def showProductView(request):
    records=Products.objects.all()
    template_name='Products/ShowProduct.html'
    context={'records':records}
    return render(request,template_name, context)


def updateProductView(request,id_fe):
    record=Products.objects.get(id=id_fe)
    form = ProductsModelForm(instance=record)
    if request.method == 'POST':
        form = ProductsModelForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('showproduct')

    template_name = 'Products/UpdateProduct.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteProductView(request,id_fe):
    record=Products.objects.get(id=id_fe)
    record.delete()
    return redirect('showproduct')