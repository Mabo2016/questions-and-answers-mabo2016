# Generated by Django 2.1 on 2018-10-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20181005_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(blank=True, help_text='Explain the question in detail', null=True),
        ),
    ]