# Generated by Django 4.1.6 on 2023-04-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_phone_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orderlar',
            },
        ),
    ]
