# Generated by Django 3.1.6 on 2021-02-07 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210207_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at'),
        ),
    ]
