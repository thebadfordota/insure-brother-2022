from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import ProfileListView, CreateProduct, MessageListView, ProductUpdateView, ProductDeleteView, \
    LoginView, RegisterUserCreateView


class TestUrls(SimpleTestCase):
    """
    Данный класс производит тестирование URL-адресов приложения 'accounts'.
    """

    def test_profile_url_resolves(self):
        url = reverse('accounts:profile')
        self.assertEquals(resolve(url).func.view_class, ProfileListView)

    def test_create_product_url_resolves(self):
        url = reverse('accounts:create_product')
        self.assertEquals(resolve(url).func.view_class, CreateProduct)

    def test_view_send_message_url_resolves(self):
        url = reverse('accounts:view_send_message', kwargs={"product_id": 1})
        self.assertEquals(resolve(url).func.view_class, MessageListView)

    def test_update_product_url_resolves(self):
        url = reverse('accounts:update_product', kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, ProductUpdateView)

    def test_delete_product_url_resolves(self):
        url = reverse('accounts:delete_product', kwargs={"pk": 1})
        self.assertEquals(resolve(url).func.view_class, ProductDeleteView)

    def test_login_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_register_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEquals(resolve(url).func.view_class, RegisterUserCreateView)
