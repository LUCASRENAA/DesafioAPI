# Generated by Django 3.1.3 on 2021-10-13 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('naner', '0010_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]
