# Generated by Django 3.1.3 on 2020-11-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
