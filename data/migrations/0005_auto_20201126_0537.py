# Generated by Django 3.1.3 on 2020-11-26 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20201126_0517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languages',
            old_name='level',
            new_name='lv',
        ),
        migrations.RemoveField(
            model_name='skils',
            name='level',
        ),
    ]