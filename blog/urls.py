from django.urls import path
from .views import *

urlpatterns = [
    
    path('', blogsPost, name='blog-view'),

]
