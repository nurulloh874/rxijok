# Generated by Django 5.1.3 on 2025-01-25 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog_id',
            new_name='blog',
        ),
    ]
