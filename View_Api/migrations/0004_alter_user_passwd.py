# Generated by Django 4.2.5 on 2023-09-20 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View_Api', '0003_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='passwd',
            field=models.CharField(max_length=500),
        ),
    ]