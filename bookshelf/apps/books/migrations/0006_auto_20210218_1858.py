# Generated by Django 3.1.6 on 2021-02-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210218_1856'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Reader',
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name_plural': 'Читатели'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AddField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(to='books.Reader'),
        ),
    ]
