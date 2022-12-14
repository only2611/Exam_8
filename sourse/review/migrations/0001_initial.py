# Generated by Django 4.1 on 2022-08-27 07:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='наименование')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('food', 'Еда'), ('tech', 'Бытовая техника'), ('tools', 'Инструменты'), ('toys', 'Игрушки')], default='other', max_length=20, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Recall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('sms', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('rate', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('moderate', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recallz', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recalls', to='review.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'db_table': 'recalls',
            },
        ),
    ]
