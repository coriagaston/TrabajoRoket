# Generated by Django 3.0 on 2021-08-23 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pregunta', '0002_auto_20210823_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='la_pregunta',
            field=models.TextField(verbose_name='Texto de la pregunta'),
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Puntaje Total')),
                ('usuarios', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es tu respuesta correcta?')),
                ('puntaje', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Su puntaje')),
                ('Usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pregunta.Usuarios')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pregunta.Pregunta')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='pregunta.Respuesta')),
            ],
        ),
    ]
