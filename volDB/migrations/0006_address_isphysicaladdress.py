# Generated by Django 2.1.7 on 2019-04-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volDB', '0005_auto_20190402_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='isPhysicalAddress',
            field=models.BooleanField(db_column='isPhysicalAddress', default=False),
            preserve_default=False,
        ),
    ]
