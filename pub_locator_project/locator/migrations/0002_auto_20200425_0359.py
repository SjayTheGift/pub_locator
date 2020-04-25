# Generated by Django 3.0.5 on 2020-04-25 03:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubinfo',
            name='contact_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='pubinfo',
            name='postal_code',
            field=models.CharField(max_length=4, validators=[django.core.validators.RegexValidator('^\\d{0,4}$')]),
        ),
    ]
