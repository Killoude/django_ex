from django.http import HttpResponse
from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views import generic
from .models import Products
from .forms import ProductForm

data_per_pages = 20

#surat jalan, transaction, product top 5 
def index(request):
    return render(request, 'fd/index.html', {'':''})


def product_create(request, product_id = None):
    """
    create and edit product here
    """
    if product_id:
        product = Products.objects.get(id= product_id)
    else:
        product = Products()
    #POSTの際
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            product = form.save(commit=False)
            try:
                product.save()
                messages.success(request, 'Product has been saved.')
            except DatabaseError:
                messages.error(request,  'something wrong.')
            return redirect('fd:product_index')
    else:
        form = ProductForm(instance = product)
    #return render(request, 'fd/product/add.html', {'form': form, 'product_id': product_id})
    return render(request, 'fd/product/add.html', dict(form=form, product_id=product_id))


def product_create_do(request):
    return HttpResponse("do create product")


def product_detail(request, product_id):
    product = Products.objects.filter(id= product_id)
    return render(request, 'fd/product/detail.html', {'product':product,'prod_id':product_id})


def product_index(request):
    all_products = Products.objects.all()
    paginator = Paginator(all_products, data_per_pages)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'fd/product/index.html', {'products': products})

def product_update(request, product_id):
    return HttpResponse("update products")

def transaction_index(request):
    return HttpResponse("transaction list (一覧)")