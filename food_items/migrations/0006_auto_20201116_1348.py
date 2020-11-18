# Generated by Django 3.1.1 on 2020-11-16 08:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0005_auto_20201114_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='created',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='created',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]