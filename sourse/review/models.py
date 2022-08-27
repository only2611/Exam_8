from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Еда'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты'),
    ('toys', 'Игрушки'),
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract=True



class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name="наименование",)
    category = models.CharField(max_length=20, default=DEFAULT_CATEGORY, choices=CATEGORY_CHOICES,
                                verbose_name='Категория')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    picture = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Картинка")

    def __str__(self):
        return f"{self.id}.{self.name} - {self.description} {self.category} - {self.picture}"

    def get_absolute_url(self):
        return reverse("review:product-view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Recall(BaseModel):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", related_name="recalls")
    product = models.ForeignKey("review.Product", on_delete=models.CASCADE, verbose_name="Товар", related_name="recalls")
    sms = models.TextField(max_length=500, verbose_name="Текст отзыва")
    rate = models.IntegerField(verbose_name='Оценка', default=5, validators=(MinValueValidator(1), MaxValueValidator(5),))
    moderate = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id}.{self.author} - {self.product} {self.sms} - {self.rate} - {self.moderate}"


    class Meta:
        db_table = "recalls"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"











