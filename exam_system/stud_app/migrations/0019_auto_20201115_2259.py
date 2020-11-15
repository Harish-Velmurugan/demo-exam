# Generated by Django 3.1.3 on 2020-11-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0018_auto_20201115_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='phone_no',
            field=models.CharField(blank=True, help_text='10-digit phone number', max_length=10, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='year_joined',
            field=models.DateField(blank=True, null=True),
        ),
    ]