# Generated by Django 3.0 on 2020-06-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0007_auto_20200617_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='内容'),
        ),
    ]
