# Generated by Django 2.1.7 on 2019-03-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volDB', '0008_auto_20190226_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(db_column='phone', max_length=20),
        ),
    ]