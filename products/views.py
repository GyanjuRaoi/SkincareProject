from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Product

class ProductList(ListView):
    model = Product
    template_name = 'home/home.html'
    context_object_name = 'products'

class CreateProduct(LoginRequiredMixin,CreateView):
    model = Product
    fields = ['name', 'description', 'productImage', 'productType']

    def form_valid(self, form):
        form.instance.user = self.request.user

        if self.request.FILES:
            form.instance.productImage = self.request.FILES['productImage']

        return super().form_valid(form)

class UpdateProduct(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'productImage', 'productType']
    

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False

class DeleteProduct(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/product/home'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False

class DetailProduct(DeleteView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
