# Generated by Django 2.2.12 on 2020-07-06 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20200706_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='p1',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='p2',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='p3',
            field=models.TextField(default='-'),
        ),
    ]
