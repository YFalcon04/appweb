# Generated by Django 5.0.1 on 2024-11-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('precio', models.IntegerField()),
                ('sector', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
