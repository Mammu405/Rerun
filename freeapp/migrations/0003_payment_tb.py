# Generated by Django 4.1.4 on 2023-01-21 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freeapp', '0002_rename_payment_tb_payment_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Freebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freeapp.f_bokking_tb')),
            ],
        ),
    ]