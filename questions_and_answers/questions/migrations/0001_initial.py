# Generated by Django 2.1 on 2018-10-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='This will be displayed when browsing the list of questions', max_length=100, null=True)),
                ('date_time_posted', models.DateField(auto_now=True)),
                ('description', models.CharField(blank=True, help_text='Explain the question in detail', max_length=5000, null=True)),
                ('up_votes_count', models.IntegerField(blank=True, null=True)),
                ('down_votes_count', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
