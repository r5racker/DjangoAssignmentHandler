# Generated by Django 3.0.2 on 2020-03-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageSubmissions', '0004_auto_20200315_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_marks_logic',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_marks_quality',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_marks_uniqueness',
            field=models.IntegerField(null=True),
        ),
    ]
