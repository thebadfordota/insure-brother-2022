from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, ListView
from .models import ClientMessage, Product
from .forms import ClientMessageForm


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


class ShowProductDetailView(DetailView):
    """
    View для отображения подробной информации о конкретном продукте.
    """
    model = Product
    template_name = 'main/show-product.html'
    query_pk_and_slug = True
    # pk_url_kwarg = 'pk'
    context_object_name = 'product_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = kwargs["object"]
        context['heading'] = kwargs["object"]
        return context


class SendMessageCreateView(CreateView):
    """
    View для отправки заявки строховой компании.
    """
    model = ClientMessage
    template_name = 'accounts/form-template.html'
    form_class = ClientMessageForm
    query_pk_and_slug = True

    def get_success_url(self):
        return f'/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отправить заявку'
        context['heading'] = 'Отправить заявку'
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['product_key'] = Product.objects.get(pk=self.kwargs['pk'])
        return initial