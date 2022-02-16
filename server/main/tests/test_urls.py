from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import ProductListView, ShowProductDetailView, SendMessageCreateView


class TestUrls(SimpleTestCase):
    """
    Данный класс производит тестирование URL-адресов приложения 'main'.
    """
    def test_home_url_resolves(self):
        url = reverse('main:home')
        self.assertEquals(resolve(url).func.view_class, ProductListView)

    def test_show_product_url_resolves(self):
        url = reverse('main:show_product', kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, ShowProductDetailView)

    def test_create_message_url_resolves(self):
        url = reverse('main:create_message', kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, SendMessageCreateView)
