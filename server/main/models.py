from django.db import models
import django.utils.timezone
from accounts.models import Company


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Product(BaseModel):
    """
    Модель продукта страховой компании.
    """
    name = models.CharField(max_length=100, verbose_name="Название")
    appearance_date = models.DateField(default=django.utils.timezone.now, verbose_name="Дата появления")
    price = models.IntegerField(verbose_name="Ежемесячная цена")
    duration_of_action = models.IntegerField(verbose_name="Длительность действия в месяцах")
    about_product = models.CharField(blank=True, max_length=100, verbose_name="О продукте")
    is_published = models.BooleanField(blank=True, default=True, verbose_name="Опубликовать")
    company_key = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'
        ordering = ['-appearance_date']

    def __str__(self):
        return self.name


class ClientMessage(BaseModel):
    """
    Модель для заявки на продукт компании.
    """
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    phone = models.CharField(blank=True, max_length=20, null=True, verbose_name="Номер телефона")
    email = models.EmailField(max_length=254, verbose_name='Электронная почта')
    appearance_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Дата отправки")
    product_key = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ['-appearance_date']

    def __str__(self):
        return str(self.last_name) + " " + str(self.appearance_date)
