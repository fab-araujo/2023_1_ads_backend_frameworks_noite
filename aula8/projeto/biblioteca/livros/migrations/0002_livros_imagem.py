# Generated by Django 4.1.3 on 2023-05-11 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='imagem',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]