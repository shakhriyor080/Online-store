# Generated by Django 4.1.6 on 2023-04-05 21:08

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
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='Sarlavha')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='Manzil')),
                ('description', models.CharField(db_index=True, max_length=255, verbose_name='Qisqacha malumot')),
                ('image', models.ImageField(db_index=True, upload_to='', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Postlar',
            },
        ),
    ]
