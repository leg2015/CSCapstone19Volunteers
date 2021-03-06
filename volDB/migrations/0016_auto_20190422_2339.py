# Generated by Django 2.1.7 on 2019-04-22 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volDB', '0015_auto_20190416_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='orgID',
            field=models.ForeignKey(db_column='orgID', on_delete=django.db.models.deletion.CASCADE, to='volDB.Organization'),
        ),
        migrations.AlterField(
            model_name='email',
            name='orgID',
            field=models.ForeignKey(db_column='orgID', on_delete=django.db.models.deletion.CASCADE, to='volDB.Organization'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='orgID',
            field=models.ForeignKey(db_column='orgID', on_delete=django.db.models.deletion.CASCADE, to='volDB.Organization'),
        ),
    ]
