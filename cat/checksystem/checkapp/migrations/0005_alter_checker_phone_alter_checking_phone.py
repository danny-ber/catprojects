# Generated by Django 5.0.6 on 2024-05-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkapp', '0004_alter_check_record_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checker',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='checking',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
