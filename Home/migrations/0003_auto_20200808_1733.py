# Generated by Django 3.0.8 on 2020-08-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_signup_whats'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T1', models.CharField(max_length=20)),
                ('Date', models.CharField(max_length=20)),
                ('Cat', models.CharField(max_length=20)),
                ('Disc', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='signup',
            name='Pic',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='PubgID',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='whats',
        ),
    ]