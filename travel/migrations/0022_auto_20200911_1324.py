# Generated by Django 3.0.8 on 2020-09-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0021_merge_20200911_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(help_text=' Enter 1 - 5', null=True),
        ),
    ]
