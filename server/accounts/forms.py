from django import forms
from .models import Company
from main.models import Product


class ProductForm(forms.ModelForm):
    """
    Форма для продукта компании.
    """
    class Meta:
        model = Product
        fields = ['name', 'appearance_date', 'price', 'duration_of_action', 'about_product', 'company_key',
                  'is_published']


class LoginForm(forms.ModelForm):
    """
    Форма авторизации.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Название компании'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not Company.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Компания с названием {username} не найдена в системе.')
        user = Company.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data

    class Meta:
        model = Company
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    """
    Форма регистрации.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    about_company = forms.CharField(required=False, max_length=1000)
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Название компании'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердить пароль'
        self.fields['email'].label = 'Электронная почта'
        self.fields['about_company'].label = 'О компании'
        self.fields['image'].label = 'Логотип'

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Company
        fields = ['username', 'password', 'confirm_password', 'email', 'about_company', 'image']