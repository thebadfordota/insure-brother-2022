from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, ListView
from .models import ClientMessage, Product
from .forms import ClientMessageForm, ProductFilterForm
from .services import ProductFilterServices
from .documents import ProductDocument


class ProductListView(ListView):
    """
    View для отображения списка продуктов.
    """
    model = Product
    template_name = "main/index.html"
    context_object_name = "product_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductFilterForm(self.request.POST)
        context['title'] = 'Все предложения'
        context['heading'] = 'Все предложения'
        return context

    # def post(self, request, *args, **kwargs):
    #     # context = self.get_context_data()  # Не получается унаследовать старый 'context'
    #     form = ProductFilterForm(request.POST)
    #     product_info = ProductDocument.search()
    #     product_info = ProductFilterServices(form, product_info).get_filtered_fields()
    #     context = {'product_info': product_info, 'form': form, 'title': 'Все предложения', 'heading': 'Все предложения'}
    #     return render(request, self.template_name, context)

    def get_queryset(self):
        product_info = Product.objects.filter(is_published=True)
        return product_info
        # context = self.get_context_data()
        # form = ProductFilterForm(self.request.POST)
        # if form.is_valid():
        #     if form.cleaned_data['price']:
        #         product_info = product_info.filter(price=form.cleaned_data['price'])
        #     if form.cleaned_data['duration_of_action']:
        #         product_info = product_info.filter(duration_of_action=form.cleaned_data['duration_of_action'])
        #     if form.cleaned_data['appearance_date']:
        #         product_info = product_info.filter(appearance_date=form.cleaned_data['appearance_date'])
        #     if form.cleaned_data['product_name']:
        #         product_info = product_info.filter(product_name=form.cleaned_data['product_name'])


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