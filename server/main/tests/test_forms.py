from django.test import TestCase
from main.forms import ProductFilterForm, ClientMessageForm
from accounts.models import Company
from main.models import Product


class TestForms(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(
            password='super_password',
            username='insure_test',
            email='123@mail.com',
            about_company='super test company',
        )
        self.product1 = Product.objects.create(
            name='test',
            price=9999,
            duration_of_action=12,
            about_product='test product',
            company_key=self.company1
        )

    def test_product_filter_form(self):
        form = ProductFilterForm(data={
            'price': 12345,
            'duration_of_action': 12,
            'appearance_date': '2022-02-15',
            'product_name': 'книга'
        })
        self.assertTrue(form.is_valid())

    def test_client_message_form(self):
        form = ClientMessageForm(data={
            'last_name': 'Сидоров',
            'first_name': 'Иван',
            'patronymic': 'Иванович',
            'email': 'test@gmail.su',
            'product_key': self.product1,
            'appearance_date': '2022-02-14',
            'phone': '88005553535'
        })
        self.assertTrue(form.is_valid())
