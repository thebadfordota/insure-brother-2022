from django.shortcuts import render
from django.views.generic import CreateView, DetailView, FormView, ListView
from .models import ClientMessage, Product


def home_page(request):
    """
    View для главной страницы.
    """
    # product_info = ProductDocument.search()
    # form = ProductFilterForm(request.POST)
    # product_filter_service = ProductFilterServices(form, product_info)
    # product_info = product_filter_service.product_filter()
    # paginator = Paginator(product_info, 6)
    # page_number = request.GET.get('page')

    # page_obj = paginator.get_page(page_number)
    context = {
        # 'form': form,
        'title': 'Все предложения',
        'heading': 'Все предложения',
        # 'product_info': product_info,
        # 'page_obj': page_obj
    }
    return render(request, "main/index.html", context)


class ProductListView(ListView):
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
