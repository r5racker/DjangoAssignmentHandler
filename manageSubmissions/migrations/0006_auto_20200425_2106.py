# Generated by Django 3.0.2 on 2020-04-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageSubmissions', '0005_auto_20200316_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='assign_id',
            field=models.IntegerField(),
        ),
    ]