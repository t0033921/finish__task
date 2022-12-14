# Generated by Django 4.1.3 on 2022-11-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='сообщение', max_length=50, verbose_name='Заголовок')),
                ('anons', models.CharField(default='Анос', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('data', models.DateTimeField(verbose_name='Дата публикации')),
            ],
        ),
    ]
