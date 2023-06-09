# Generated by Django 4.1.7 on 2023-04-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
