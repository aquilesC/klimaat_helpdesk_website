# Generated by Django 3.1.2 on 2021-03-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210307_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='original_question',
            field=models.TextField(blank=True, null=True, verbose_name='Backup information'),
        ),
    ]
