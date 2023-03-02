# Generated by Django 4.1.7 on 2023-03-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("songs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="song",
            name="NME_rank",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="song",
            name="UG_favourites",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="song",
            name="UG_views",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="song",
            name="rank",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="song",
            name="rolling_stone_rank",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="song",
            name="year_release",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]