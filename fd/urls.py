from django.urls import path

from . import views

app_name = 'fd'

urlpatterns = [
    # ex: /fd/
    path('', views.index, name = 'index'),
    # /fd/product 一覧

    #path('product', views.product_index, name = 'product_index'),
    path('product',views.ProductIndex.as_view(), name = 'product_index'),
    path('product/create', views.ProductDataInput.as_view(), name= 'product_data_input'),
    path('product/confirm_create', views.ProductDataConfirm.as_view(), name ="product_data_confirm"),
    path('product/create_save', views.ProductDataCreate.as_view(), name ="product_data_create"),
    path('product/update/<int:product_id>', views.product_update, name='product_update'),
    # POST
    #path('product/edit/<int:product_id>', views.product_create, name = 'update_product'),
    # path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    # # ex: /polls/5/results/ 
    path('transaction', views.transaction_index, name = 'transaction_index'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name ='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name = 'vote'),
]