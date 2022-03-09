from django.views.generic import CreateView, DetailView, ListView
from .models import ClientMessage, Product
from .forms import ClientMessageForm, ProductFilterForm
from .services import ProductFilterServices
from .tasks import send_user_info
from accounts.services import CountViewsServices


class ProductListView(ListView):
    """
    View для отображения списка продуктов.
    """
    paginate_by = 6
    model = Product
    template_name = "main/index.html"
    context_object_name = "product_info"

    def get_queryset(self):
        return ProductFilterServices(ProductFilterForm(self.request.GET)).get_filtered_fields()  # ElasticSearch

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductFilterForm(self.request.GET)
        context['title'] = 'Все предложения'
        context['heading'] = 'Все предложения'
        return context


class ShowProductDetailView(DetailView):
    """
    View для отображения подробной информации о конкретном продукте.
    """
    model = Product
    template_name = 'main/show-product.html'
    query_pk_and_slug = True
    context_object_name = 'product_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = kwargs["object"]
        context['heading'] = kwargs["object"]
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        product_info = Product.objects.get(pk=self.kwargs["pk"])
        CountViewsServices(int(self.kwargs["pk"])).increase_count_views(product_info.name)  # Mongo
        return response


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

    def form_valid(self, form):
        form.save()
        current_company = form.cleaned_data.get('product_key')
        company_key = current_company.company_key
        company_email = company_key.email if company_key else None
        customer_info = {
            'last_name': str(form.cleaned_data['last_name']),
            'first_name': str(form.cleaned_data['first_name']),
            'patronymic': str(form.cleaned_data['patronymic']),
            'phone': str(form.cleaned_data['phone']),
            'email': str(form.cleaned_data['email']),
            'appearance_date': str(form.cleaned_data['appearance_date']),
            'product_key': str(form.cleaned_data['product_key']),
            'company_email': str(company_email),
        }
        print(customer_info)
        send_user_info.delay(customer_info)  # celery task
        return super().form_valid(form)
