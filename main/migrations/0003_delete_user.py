# Generated by Django 4.1.7 on 2023-04-26 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_users_delete_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
