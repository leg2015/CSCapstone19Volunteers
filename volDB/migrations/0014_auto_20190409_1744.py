# Generated by Django 2.1.7 on 2019-04-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volDB', '0013_auto_20190403_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(db_column='city', max_length=50),
        ),
    ]
