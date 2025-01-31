# Generated by Django 4.1.3 on 2023-01-24 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='days',
        ),
        migrations.AddField(
            model_name='menu',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], default='0', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='time',
            field=models.CharField(choices=[('0', 'Morning'), ('1', 'AfterNoon'), ('2', 'Night')], max_length=1),
        ),
        migrations.AlterField(
            model_name='noteatingtoday',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=1),
        ),
        migrations.AlterField(
            model_name='noteatingtoday',
            name='time',
            field=models.CharField(choices=[('0', 'Morning'), ('1', 'AfterNoon'), ('2', 'Night')], max_length=1),
        ),
        migrations.AlterField(
            model_name='noteatingtoday',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='silvertoken',
            name='day',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=1),
        ),
        migrations.AlterField(
            model_name='silvertoken',
            name='time',
            field=models.CharField(choices=[('0', 'Morning'), ('1', 'AfterNoon'), ('2', 'Night')], max_length=1),
        ),
    ]
