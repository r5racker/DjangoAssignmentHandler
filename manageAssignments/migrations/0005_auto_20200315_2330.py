# Generated by Django 3.0.2 on 2020-03-15 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageAssignments', '0004_auto_20200315_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assign_file',
            field=models.FileField(null=True, upload_to='files'),
        ),
    ]