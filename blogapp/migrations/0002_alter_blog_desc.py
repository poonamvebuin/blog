# Generated by Django 4.0.5 on 2022-07-18 07:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Desc',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]