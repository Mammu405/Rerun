# Generated by Django 4.1.4 on 2023-03-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeapp', '0005_bank_details_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='webreview_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
