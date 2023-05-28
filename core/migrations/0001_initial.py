# Generated by Django 4.1 on 2023-05-23 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Esp32',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField(null=True)),
                ('longitude', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('cidade', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicoesRio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altura', models.DecimalField(decimal_places=3, max_digits=100, null=True)),
                ('dat_medicao', models.DateTimeField(null=True)),
                ('esp32_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.esp32')),
            ],
        ),
        migrations.AddField(
            model_name='esp32',
            name='rio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.rio'),
        ),
    ]
