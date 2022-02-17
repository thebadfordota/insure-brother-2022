from django.test import TestCase
from main.models import Product, ClientMessage
from accounts.models import Company


class TestModels(TestCase):
    """
    Данный класс производит тестирование моделей приложения 'main'.
    """

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
        self.client_message1 = ClientMessage.objects.create(
            last_name='Сидоров',
            first_name='Иван',
            patronymic='Иванович',
            email='test@gmail.su',
            product_key=self.product1
        )

    def test_product(self):
        product = Product.objects.get(name="test")
        self.assertEquals(str(product), 'test')

    def test_client_message(self):
        client_message = ClientMessage.objects.get(email="test@gmail.su")
        self.assertEquals(str(client_message), 'Сидоров Иван')
