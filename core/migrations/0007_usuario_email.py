# Generated by Django 4.1 on 2023-05-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_funcionario_usuariologin_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
