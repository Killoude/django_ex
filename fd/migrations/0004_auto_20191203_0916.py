# Generated by Django 2.2.7 on 2019-12-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd', '0003_auto_20191203_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_transaction',
            name='crt',
            field=models.IntegerField(),
        ),
    ]
