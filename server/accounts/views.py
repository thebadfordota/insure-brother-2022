from main.models import Product, ClientMessage
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, UpdateView, DeleteView, CreateView
from .models import Company
from .forms import LoginForm, RegisterForm, ProductForm
from django.contrib.auth import authenticate, login


def view_profile(request):
    """
    View для профиля компании.
    """
    product_info = Product.objects.filter(company_key=request.user.id)
    context = {'title': 'Профиль', 'product_info': product_info}
    return render(request, 'accounts/profile.html', context)


def view_send_message(request, product_id):
    """
    View для просмотра всех заявок на определённый продукт.
    """
    message_info = ClientMessage.objects.filter(product_key=product_id)
    context = {
        'title': 'Все сообщения',
        'heading': 'Все сообщения',
        'message_info': message_info
    }
    return render(request, 'accounts/message.html', context)


class CreateProduct(CreateView):
    model = Product
    template_name = 'accounts/form-template.html'
    form_class = ProductForm
    query_pk_and_slug = True

    def get_success_url(self):
        return f'/'

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


class ProductUpdateView(UpdateView):
    """
    View для изменения записи в таблице 'Product'.
    """
    model = Product
    template_name = 'accounts/form-template.html'
    form_class = ProductForm

    def get_success_url(self):
        return f'/accounts/profile/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить продукт'
        context['heading'] = 'Обновить продукт'
        return context


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
        return f'/accounts/profile/'


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


class RegisterView(View):
    """
    View для регистрации пользователя.
    """
    def get(self, request):
        form = RegisterForm(self.request.POST or None)
        context = {'form': form, 'title': 'Регистрация', 'heading': 'Зарегистрироваться'}
        return render(request, 'accounts/form-template.html', context)

    def post(self, request):
        form = RegisterForm(self.request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.about_company = form.cleaned_data['about_company']
            new_user.image = form.cleaned_data['image']
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect(reverse('main:home'))
        context = {'form': form, 'title': 'Регистрация', 'heading': 'Зарегистрироваться'}
        return render(request, 'accounts/form-template.html', context)

