# Generated by Django 4.1.7 on 2023-03-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProjectstones4', '0003_rename_idnumber_employees_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]