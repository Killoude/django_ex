# Generated by Django 3.0 on 2019-12-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd', '0008_auto_20191203_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='nota',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
