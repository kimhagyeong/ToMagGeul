# Generated by Django 3.1.1 on 2020-10-15 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomaggeultext', '0003_auto_20201015_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmtext',
            name='text_cover',
            field=models.ImageField(default='../static/img/no-image.png', upload_to='covers'),
        ),
    ]
