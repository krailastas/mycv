# Generated by Django 3.1.3 on 2020-11-25 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20201124_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['-order']},
        ),
        migrations.AlterModelOptions(
            name='main',
            options={'ordering': ['-order']},
        ),
        migrations.AddField(
            model_name='jobs',
            name='main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='data.main'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='order',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='order',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='own_site',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='main',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='data/photo'),
        ),
        migrations.AlterField(
            model_name='main',
            name='full_name',
            field=models.CharField(blank=True, max_length=128, unique=True),
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=258)),
                ('order', models.IntegerField(blank=True, default=1, null=True)),
                ('main', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='data.main')),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
    ]
