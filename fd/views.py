from django.http import HttpResponse
from django.contrib import messages
from django.db import DatabaseError
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.views import generic
from django.urls import reverse_lazy
from .models import Products
from .forms import ProductForm

data_per_pages = 20

#surat jalan, transaction, product top 5 
def index(request):
    return render(request, 'fd/index.html', {'':''})

class ProductDataInput(generic.FormView):
    """just showing the input form"""
    template_name = 'fd/product/add.html'
    form_class = ProductForm

    def form_valid(self, form):
        return render(self.request, 'fd/product/add.html', {'form':form})

class ProductDataConfirm(generic.FormView):
    """show the confirmation form"""
    template_name = 'fd/product/add.html'
    form_class = ProductForm

    def form_valid(self, form):
        return render(self.request, 'fd/product/confirm_add.html', {'form': form})
    
    def form_invalid(self, form):
        return render(self.request, 'fd/product/add.html', {'form': form})

class ProductDataCreate(generic.CreateView):
    """ユーザーデータの登録ビュー。ここ以外では、CreateViewを使わないでください"""
    form_class = ProductForm
    success_url = reverse_lazy('fd:product_index')
    template_name = 'fd/product/add.html'

    def form_invalid(self, form):
        """基本的にはここに飛んでこないはずです。UserDataConfirmでバリデーションは済んでるため"""
        return render(self.request, 'fd/product/add.html', {'form': form})
    
    def form_valid(self, form):
        try:
            messages.success(self.request, "Product has been saved.")
        except DatabaseError:
            messages.error(self.request,  'something wrong.')
        return super().form_valid(form)

def product_update(request, product_id):
    """
    Edit product here
    """
    if product_id:
        product = Products.objects.get(id= product_id)
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
    return render(request, 'fd/product/edit.html', dict(form=form, product_id=product_id))


def product_detail(request, product_id):
    product = Products.objects.filter(id= product_id)
    return render(request, 'fd/product/detail.html', {'product':product,'prod_id':product_id})


class ProductIndex(generic.ListView):
    template_name = 'fd/product/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        """Return the products based on search."""
        query = self.request.GET.get('q')
        if query:
            product = Products.objects.filter(code__icontains=query)
            #return Products.objects.filter(code__icontains=query)
        else:
            product = Products.objects.all()
            #return Products.objects.all()
        paginator = Paginator(product, data_per_pages)
        page = self.request.GET.get('page')
        products = paginator.get_page(page)
        return products

def product_index(request):
    all_products = Products.objects.all()
    paginator = Paginator(all_products, data_per_pages)

    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request, 'fd/product/index.html', {'products': products})

def transaction_index(request):
    return HttpResponse("transaction list (一覧)")