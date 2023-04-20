# Generated by Django 4.0.3 on 2023-04-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('A', 'Admin'), ('M', 'Manager'), ('C', 'Customer'), ('U', 'Unkown')], default='U', max_length=1),
        ),
    ]
