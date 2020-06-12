# Generated by Django 3.0.6 on 2020-05-28 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mmt_map', '0013_auto_20200527_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_audiofile_line', to='mmt_map.Line'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_audiofile_point', to='mmt_map.Point'),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='polygon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_audiofile_polygon', to='mmt_map.Polygon'),
        ),
        migrations.AlterField(
            model_name='document',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_document_line', to='mmt_map.Line'),
        ),
        migrations.AlterField(
            model_name='document',
            name='point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_document_point', to='mmt_map.Point'),
        ),
        migrations.AlterField(
            model_name='document',
            name='polygon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_document_polygon', to='mmt_map.Polygon'),
        ),
        migrations.AlterField(
            model_name='image',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_image_line', to='mmt_map.Line'),
        ),
        migrations.AlterField(
            model_name='image',
            name='point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_image_point', to='mmt_map.Point'),
        ),
        migrations.AlterField(
            model_name='image',
            name='polygon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mmt_map_image_polygon', to='mmt_map.Polygon'),
        ),
    ]
