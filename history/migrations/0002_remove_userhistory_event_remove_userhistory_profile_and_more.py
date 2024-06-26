# Generated by Django 5.0.1 on 2024-01-15 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_userprofile_is_available'),
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhistory',
            name='event',
        ),
        migrations.RemoveField(
            model_name='userhistory',
            name='profile',
        ),
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donation_request', to='account.bloodgroup')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donation_request', to='account.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonationReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='account.userprofile')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='history.donationrequest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='UserHistory',
        ),
    ]
