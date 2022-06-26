# Generated by Django 2.2.27 on 2022-06-25 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='love_bao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_def', models.CharField(max_length=100)),
                ('banner_pic', models.ImageField(upload_to='images/')),
                ('left_bao_pic', models.ImageField(upload_to='images/')),
                ('left_bao_ig', models.CharField(max_length=200)),
                ('left_bao_des', models.CharField(max_length=500)),
                ('right_bao_pic', models.ImageField(upload_to='images/')),
                ('right_bao_ig', models.CharField(max_length=200)),
                ('rights_bao_des', models.CharField(max_length=500)),
                ('bao_together_date', models.DateTimeField()),
                ('bao_bao_talk', models.CharField(max_length=500)),
                ('bao_big_thing_date1', models.DateTimeField()),
                ('bao_big_thing_des1', models.CharField(max_length=50)),
                ('bao_big_thing_date2', models.DateTimeField()),
                ('bao_big_thing_des2', models.CharField(max_length=50)),
                ('bao_big_thing_date3', models.DateTimeField()),
                ('bao_big_thing_des3', models.CharField(max_length=50)),
                ('bao_big_thing_date4', models.DateTimeField()),
                ('bao_big_thing_des4', models.CharField(max_length=50)),
                ('bao_six_pic1', models.ImageField(upload_to='images/')),
                ('bao_six_pic2', models.ImageField(upload_to='images/')),
                ('bao_six_pic3', models.ImageField(upload_to='images/')),
                ('bao_six_pic4', models.ImageField(upload_to='images/')),
                ('bao_six_pic5', models.ImageField(upload_to='images/')),
                ('bao_six_pic6', models.ImageField(upload_to='images/')),
                ('user_account_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
