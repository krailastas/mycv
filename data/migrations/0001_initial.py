# Generated by Django 3.1.3 on 2020-11-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=256)),
                ('start', models.DateField(blank=True)),
                ('end', models.DateField(blank=True)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('company', models.CharField(blank=True, max_length=128)),
                ('general_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_text', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('full_name', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
