# Generated by Django 2.2.7 on 2019-12-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(),
        ),
    ]