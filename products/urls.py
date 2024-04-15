from django.urls import path
from .views import *

urlpatterns = [

    path('create', CreateProduct.as_view(), name='create_product'),
    path('update/<int:pk>', UpdateProduct.as_view() , name='update_product' ),
    path('delete/<int:pk>', DeleteProduct.as_view(), name='delete_product'),
    path('home/', ProductList.as_view(), name='home_page' ),
    path('detail/<int:pk>', DetailProduct.as_view(), name='detail_product' ),
    
]
