# Generated by Django 3.1.3 on 2020-11-22 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
