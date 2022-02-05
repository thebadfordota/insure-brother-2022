from django.urls import path
from .views import ProductListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    # path('', home_page, name='home'),
    path('', ProductListView.as_view(), name='home'),
    # path('<int:pk>/create/massage', SendMessageCreateView.as_view(), name='create_message'),
    # path('show/product/<slug:pk>', ShowProduct.as_view(), name='show_product')
]

urlpatterns += staticfiles_urlpatterns()
