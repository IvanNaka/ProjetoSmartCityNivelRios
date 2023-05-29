# Generated by Django 4.1 on 2023-05-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_usuariologin_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariologin',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]