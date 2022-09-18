# Generated by Django 4.0.4 on 2022-06-24 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_rename_company_id_site_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='list_houses',
            field=models.FileField(blank=True, null=True, upload_to='template_file'),
        ),
        migrations.AlterField(
            model_name='company',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.user'),
        ),
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='building_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.company'),
        ),
        migrations.AlterField(
            model_name='house',
            name='floor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='kadastr_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='total_floor_space',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='year_of_commissioning',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]