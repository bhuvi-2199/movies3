# Generated by Django 3.1.4 on 2020-12-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='test',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
