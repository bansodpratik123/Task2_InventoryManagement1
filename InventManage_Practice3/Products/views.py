from django.shortcuts import render,redirect
from .forms import ProductModelForm
from .models import Products


# Create your views here.
def homepageView(request):
    template_name='Products/Homepage.html'
    context={}
    return render(request, template_name, context)

def addProctView(request):
    form=ProductModelForm()
    if request.method=='POST':
        form=ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='Products/AddProduct.html'
    context={'form':form}
    return render(request, template_name, context)

def showProctView(request):
    records=Products.objects.all()

    template_name='Products/ShowProduct.html'
    context={'records':records}
    return render(request, template_name, context)

def updateProctView(request,id_fe):
    record = Products.objects.get(id=id_fe)
    form=ProductModelForm(instance=record)
    if request.method=='POST':
        form=ProductModelForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('showproduct')
    template_name='Products/UpdateProduct.html'
    context={'form':form}
    return render(request, template_name, context)

def deleleProductView(request,id_fe):
    record = Products.objects.get(id=id_fe)
    record.delete()
    return redirect('showproduct')