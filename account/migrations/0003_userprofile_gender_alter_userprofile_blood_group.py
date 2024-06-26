# Generated by Django 5.0.1 on 2024-01-15 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_userprofile_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='blood_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='account.bloodgroup'),
        ),
    ]
