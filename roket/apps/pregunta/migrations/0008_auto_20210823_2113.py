# Generated by Django 3.0 on 2021-08-24 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pregunta', '0007_auto_20210823_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pregunta.Respuesta'),
        ),
    ]
