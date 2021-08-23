# Generated by Django 3.0 on 2021-08-23 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pregunta', '0003_auto_20210823_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Puntaje Total')),
                ('perfil_usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='preguntasrespondidas',
            name='Usuarios',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='perfil_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pregunta.Perfil_Usuario'),
            preserve_default=False,
        ),
    ]
