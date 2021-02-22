# Generated by Django 3.1.7 on 2021-02-21 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20210218_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='RankBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('rank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.rank')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.reader')),
            ],
        ),
        migrations.AddField(
            model_name='rank',
            name='readers',
            field=models.ManyToManyField(through='books.RankBooks', to='books.Reader'),
        ),
    ]