# Generated by Django 2.2.12 on 2020-07-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='-')),
                ('pt', models.TextField(default='-')),
                ('p2', models.TextField(default='-')),
                ('p3', models.TextField(default='-')),
                ('p4', models.TextField(default='-')),
            ],
        ),
    ]
