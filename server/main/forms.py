from django import forms
from .models import ClientMessage


class ClientMessageForm(forms.ModelForm):
    """
    Форма для заявки на продукт компании.
    """
    class Meta:
        model = ClientMessage
        fields = ['last_name', 'first_name', 'patronymic', 'phone', 'email', 'product_key']


class ProductFilterForm(forms.Form):
    """
    Форма для фильтрации полей модели 'Product'.
    """
    price = forms.IntegerField(label="Цена", required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Цена'
    }))
    duration_of_action = forms.IntegerField(label="Длительность", required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Длительность'
    }))
    appearance_date = forms.DateTimeField(label="Дата появления", required=False, widget=forms.DateTimeInput(attrs={
        'class': 'form-control', 'placeholder': 'Дата появления'
    }))
    product_name = forms.CharField(label="Название продукта", required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Название продукта'
    }))