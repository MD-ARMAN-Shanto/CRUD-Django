#CRUD PROJECT
from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def product_list(request):
    pro = Product.objects.all()
    return render(request, 'products/product.html', {'pro': pro})


def create_list(request):
    form = ProductForm(request.POST or  None)

    if form.is_valid():
        form.save()
        return redirect('product')
    else:
        return render(request, 'products/create.html', {'form': form})


def update_list(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product')
    else:
        return render(request, 'products/create.html', {'form':form, 'product':product})


def delete_list(request, id):
    product = Product.objects.get(id= id)

    if request.method =='POST':
        product.delete()
        return redirect('product')

    return render(request, 'products/delete.html', {'product': product})

