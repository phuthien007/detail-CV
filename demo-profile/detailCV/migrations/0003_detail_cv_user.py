# Generated by Django 3.1.3 on 2020-11-04 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detailCV', '0002_auto_20201104_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail_cv',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
