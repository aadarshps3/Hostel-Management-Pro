# Generated by Django 3.1.3 on 2021-05-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0008_fees_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fees',
            name='paid_date',
            field=models.DateField(null=True),
        ),
    ]
