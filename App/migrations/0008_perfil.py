# Generated by Django 4.1.5 on 2023-01-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.CharField(max_length=60)),
                ('imagen', models.ImageField(upload_to='imagenes')),
            ],
        ),
    ]
