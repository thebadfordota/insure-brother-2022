from django import forms
from .models import ClientMessage


class ClientMessageForm(forms.ModelForm):
    """
    Форма для заявки на продукт компании.
    """
    class Meta:
        model = ClientMessage
        fields = ['last_name', 'first_name', 'patronymic', 'phone', 'email', 'product_key']
