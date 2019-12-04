# Generated by Django 2.2.7 on 2019-12-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd', '0004_auto_20191203_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='deleted_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='deleted_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='deleted_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='deleted_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='deleted_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
    ]