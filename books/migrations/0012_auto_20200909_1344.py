# Generated by Django 2.2.12 on 2020-09-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20200909_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='image',
            field=models.FileField(upload_to='tester/1/1/'),
        ),
    ]