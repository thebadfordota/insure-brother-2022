from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """
    Данный класс производит тестирование представлений приложения 'main'.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.home_url = reverse('main:home')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
