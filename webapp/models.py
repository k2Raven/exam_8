from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

CHOICES = [('other', 'Разное'), ('electronics', 'Электроника'), ('Services', 'Услуги'), ('Books', 'Книги')]


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    category = models.CharField(max_length=20, default='other', choices=CHOICES, verbose_name='Категории')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(verbose_name='Картинка', upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.category}"


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='reviews',
                                verbose_name='Товар')
    text = models.TextField(max_length=2000, verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])
    is_moderated = models.BooleanField(default=False, verbose_name='Подтвержден')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    def __str__(self):
        return f"{self.author.username} - {self.product.name}"
