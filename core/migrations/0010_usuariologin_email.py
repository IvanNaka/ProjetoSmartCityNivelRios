# Generated by Django 4.1 on 2023-05-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_usuariologin_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariologin',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
