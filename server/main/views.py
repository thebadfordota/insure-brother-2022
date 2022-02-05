from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, ListView
from .models import ClientMessage, Product


class ProductListView(ListView):
    """
    View для отображения списка продуктов.
    """
    model = Product
    template_name = "main/index.html"
    context_object_name = "product_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все предложения'
        context['heading'] = 'Все предложения'
        return context

    def get_queryset(self):
        return Product.objects.filter(is_published=True)
