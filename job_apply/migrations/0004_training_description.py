# Generated by Django 2.0 on 2019-03-12 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_apply', '0003_experience_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
