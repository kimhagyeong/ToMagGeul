# Generated by Django 3.1.1 on 2020-09-13 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tomaggeul', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('tmtext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tomaggeul.tmtext')),
                ('tmuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paid_subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('use_points', models.PositiveIntegerField(default=0)),
                ('remaining_points', models.PositiveIntegerField(default=0)),
                ('payment', models.PositiveIntegerField(default=0)),
                ('tmtext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tomaggeul.tmtext')),
                ('tmuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_subscription', models.BooleanField(default=False)),
                ('adress', models.CharField(max_length=200)),
                ('delivery_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('delivery_status', models.BooleanField(default=False)),
                ('tmuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]