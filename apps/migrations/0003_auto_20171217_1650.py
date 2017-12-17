# Generated by Django 2.0 on 2017-12-17 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0002_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='target_user',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='target_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='from_user',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
