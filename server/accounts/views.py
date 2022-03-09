from main.models import Product, ClientMessage
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, UpdateView, DeleteView, CreateView, ListView
from .models import Company
from .forms import LoginForm, RegisterForm, ProductForm
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .services import CountViewsServices


@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    """
    View для отображения списка продуктов.
    """
    model = Product
    template_name = "accounts/profile.html"
    context_object_name = "product_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        context['heading'] = 'Профиль'
        return context

    def get_queryset(self):
        return Product.objects.filter(company_key=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class MessageListView(ListView):
    """
    View для просмотра всех заявок на определённый продукт.
    """
    model = ClientMessage
    query_pk_and_slug = True
    template_name = "accounts/message.html"
    context_object_name = "message_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все сообщения'
        count_views = CountViewsServices()
        context['heading'] = f'Кол-во просмотров: {count_views.get_count_views(int(self.kwargs["product_id"]))}'
        return context

    def get_queryset(self):
        return ClientMessage.objects.filter(product_key=self.kwargs['product_id'])


@method_decorator(login_required, name='dispatch')
class CreateProduct(CreateView):
    """
    View для создания продукта коммпании.
    """
    model = Product
    template_name = 'accounts/form-template.html'
    form_class = ProductForm
    query_pk_and_slug = True

    def get_success_url(self):
        return '/accounts/profile/'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(CreateProduct, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать продукт'
        context['heading'] = 'Создать продукт'
        return context

    def get_initial(self, ):
        initial = super().get_initial()
        initial['company_key'] = Company.objects.get(pk=self.request.user.id)
        return initial


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    """
    View для изменения записи в таблице 'Product'.
    """
    model = Product
    template_name = 'accounts/form-template.html'
    form_class = ProductForm

    def get_success_url(self):
        return '/accounts/profile/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить продукт'
        context['heading'] = 'Обновить продукт'
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            CountViewsServices().update_count_views_info(int(self.kwargs['pk']), form.cleaned_data['name'])
        return super(ProductUpdateView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(DeleteView):
    """
    View для удаления записи из таблицы 'Product'.
    """
    model = Product
    template_name = 'accounts/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить запись'
        context['heading'] = 'Удаление продукта'
        return context

    def get_success_url(self):
        return '/accounts/profile/'


class LoginView(View):
    """
    View для авторизации пользователя.
    """
    def get(self, request):
        form = LoginForm(self.request.POST or None)
        context = {'form': form, 'title': 'Войти', 'heading': 'Войти'}
        return render(request, 'accounts/form-template.html', context)

    def post(self, request):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('main:home'))
        context = {'form': form, 'title': 'Войти', 'heading': 'Войти'}
        return render(request, 'accounts/form-template.html', context)


class RegisterUserCreateView(CreateView):
    """
    View для регистрации пользователя.
    """
    model = Company
    template_name = 'accounts/form-template.html'
    form_class = RegisterForm
    query_pk_and_slug = True

    def get_success_url(self):
        return f'/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['heading'] = 'Зарегистрироваться'
        return context
