# Generated by Django 3.1.7 on 2021-02-23 15:47

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[165, 247], upload_to='covers'),
        ),
    ]