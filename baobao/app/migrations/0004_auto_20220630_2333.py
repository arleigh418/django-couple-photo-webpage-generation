# Generated by Django 2.2.27 on 2022-06-30 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20220630_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='love_bao',
            name='user_account_name',
        ),
        migrations.AddField(
            model_name='love_bao',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
