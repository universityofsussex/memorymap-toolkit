# Generated by Django 3.0.6 on 2020-05-27 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmt_map', '0006_remove_point_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='category',
            new_name='theme',
        ),
    ]
