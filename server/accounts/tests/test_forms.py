from django.test import TestCase
from accounts.models import Company
from accounts.forms import ProductForm, LoginForm
from main.models import Product


class TestForms(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(
            password='super_password',
            username='insure_test',
            email='123@mail.com',
            about_company='super test company',
        )

    def test_product_form(self):
        form = ProductForm(data={
            'name': 'test',
            'price': 9999,
            'appearance_date': '2022-01-01',
            'duration_of_action': 12,
            'about_product': 'test product',
            'company_key': self.company1,
            'is_published': True
        })
        self.assertTrue(form.is_valid())
