# Generated by Django 5.0.7 on 2024-07-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='course/course/'),
        ),
    ]
