# Generated by Django 2.2.27 on 2022-07-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20220702_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='love_bao',
            name='bao_big_thing_title1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='love_bao',
            name='bao_big_thing_title2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='love_bao',
            name='bao_big_thing_title3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='love_bao',
            name='bao_big_thing_title4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='love_bao',
            name='left_bao_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='love_bao',
            name='right_bao_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='love_bao',
            name='bao_big_thing_des1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='love_bao',
            name='bao_big_thing_des2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='love_bao',
            name='bao_big_thing_des3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='love_bao',
            name='bao_big_thing_des4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
