from django.urls import path

from . import views

app_name = 'fd'

urlpatterns = [
    # ex: /fd/
    path('', views.index, name = 'index'),
    # /fd/product 一覧
    #customer
    path('customer', views.CustomerIndex.as_view(), name='customer_index'),
    path('customer/create', views.CustomerCreate.as_view(), name='customer_create'),
    path('customer/create_save', views.CustomerCreateDo.as_view(), name='customer_create_save'),
    path('customer/update/<int:customer_id>', views.customer_update, name ='customer_update'),
    #path('customer/create', views.transaction_index, name = 'customer_add_input'),

    #path('product', views.product_index, name = 'product_index'),
    path('product',views.ProductIndex.as_view(), name = 'product_index'),
    path('product/create', views.ProductDataInput.as_view(), name= 'product_data_input'),
    path('product/confirm_create', views.ProductDataConfirm.as_view(), name ="product_data_confirm"),
    path('product/create_save', views.ProductDataCreate.as_view(), name ="product_data_create"),
    path('product/update/<int:product_id>', views.product_update, name='product_update'),

    ##surat jalan
    #path('suratjalan', views.surat_jalan_index, name='surat_jalan_index'),
    path('suratjalan', views.SuratJalanIndex.as_view(), name='surat_jalan_index'),
    path('suratjalan/create', views.SuratJalanInput.as_view(), name = 'surat_jalan_input'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name ='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name = 'vote'),
]