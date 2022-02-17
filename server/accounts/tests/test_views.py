from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """
    Данный класс производит тестирование представлений приложения 'accounts'.
    """
    def setUp(self) -> None:
        self.client = Client()
        self.profile_url = reverse('accounts:profile')
        self.login_url = reverse('accounts:login')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/profile.html")

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/form-template.html')
