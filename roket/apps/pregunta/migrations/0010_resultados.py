# Generated by Django 3.0 on 2021-08-24 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pregunta', '0009_auto_20210824_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]