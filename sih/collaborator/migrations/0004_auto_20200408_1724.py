# Generated by Django 3.0.2 on 2020-04-08 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0003_auto_20200401_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='notification',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='destination',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
