# Generated by Django 5.0.1 on 2024-01-17 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=12)),
                ('problem', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
