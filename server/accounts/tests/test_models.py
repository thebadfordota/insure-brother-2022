from django.test import TestCase
from accounts.models import Company


class TestModels(TestCase):
    """
    Данный класс производит тестирование моделей приложения 'accounts'.
    """

    def setUp(self):
        self.company1 = Company.objects.create(
            password='super_password',
            username='insure_test',
            email='123@mail.com',
            about_company='super test company',
        )

    def test_product(self):
        company = Company.objects.get(username="insure_test")
        self.assertEquals(str(company), 'insure_test')
