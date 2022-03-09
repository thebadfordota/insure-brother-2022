from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .documents import ProductDocument


class ProductFilterServices:
    """
    Данный класс реализует фильтрацию полей таблицы 'Product'.
    """
    def __init__(self, form):
        self.form = form
        self.product_info = ProductDocument.search()

    def get_filtered_fields(self):
        if self.form.is_valid():
            if self.form.cleaned_data['price']:
                self.product_info = self.product_info.filter("term", price=self.form.cleaned_data['price'])
            if self.form.cleaned_data['duration_of_action']:
                self.product_info = self.product_info.filter("term", duration_of_action=self.form.cleaned_data[
                    'duration_of_action'])
            if self.form.cleaned_data['appearance_date']:
                self.product_info = self.product_info.query("match",
                                                            appearance_date=self.form.cleaned_data['appearance_date'])
            if self.form.cleaned_data['product_name']:
                self.product_info = self.product_info.query("match", name=self.form.cleaned_data['product_name'])
        return self.product_info.to_queryset().filter(is_published=True)


class SendEmailServices:
    """
    Данный класс реализует отправку писем на почту страховой компании.
    """
    def __init__(self, customer_info):
        self.customer_info = customer_info

    def send(self):
        if self.customer_info["company_email"]:
            html_body = render_to_string('main/email-template.html', self.customer_info)
            message = EmailMultiAlternatives(subject=f'Заявка на продукт {self.customer_info["product_key"]}',
                                             to=[self.customer_info["company_email"]])
            message.attach_alternative(html_body, "text/html")
            message.send()
        else:
            print("Некорректный email компании")
