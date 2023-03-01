# Generated by Django 4.1.7 on 2023-02-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('body', models.CharField(max_length=1000, verbose_name='Содержимое статьи')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='post_pictures/', verbose_name='Изображение')),
                ('views', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество просмотров')),
                ('published_on', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]