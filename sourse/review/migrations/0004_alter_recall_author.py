# Generated by Django 4.1 on 2022-08-27 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0003_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recall',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recalls', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
