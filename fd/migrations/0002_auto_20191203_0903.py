# Generated by Django 2.2.7 on 2019-12-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customers',
            name='deleted_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customers',
            name='updated_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='deleted_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='pcs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detail_transaction',
            name='updated_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='crt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='deleted_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='pcs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='deleted_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='created_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='deleted_by',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='role_type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_by',
            field=models.IntegerField(),
        ),
    ]