from django.urls import path

from . import views

app_name = 'fd'

urlpatterns = [
    # ex: /fd/
    path('', views.index, name = 'index'),
    # /fd/product
    path('product', views.product_index, name = 'product_index'),
    # ex /fd/product/create -->GET
    path('product/create', views.product_create, name= 'product_create'),
    # ex /fd/product/edit/1 -->GET
    path('product/edit/<int:product_id>', views.product_create, name='product_edit'),
    # POST
    path('product/edit/<int:product_id>', views.product_create, name = 'update_product'),
    # path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    # # ex: /polls/5/results/ 
    path('transaction', views.transaction_index, name = 'transaction_index'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name ='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name = 'vote'),
]