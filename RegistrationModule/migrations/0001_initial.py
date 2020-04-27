# Generated by Django 3.0.2 on 2020-03-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUsers',
            fields=[
                ('user_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('c_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=20)),
                ('c_credit', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_first_name', models.CharField(max_length=20)),
                ('student_middle_name', models.CharField(max_length=20)),
                ('student_last_name', models.CharField(max_length=20)),
                ('student_username', models.CharField(max_length=100)),
                ('student_dob', models.DateTimeField(verbose_name='date published')),
                ('student_semester', models.IntegerField()),
                ('student_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('student_address', models.CharField(max_length=200)),
                ('student_address2', models.CharField(default='NO_ADDR', max_length=200)),
                ('student_city', models.CharField(max_length=20)),
                ('student_state', models.CharField(max_length=20)),
                ('student_zip', models.CharField(max_length=7)),
                ('student_mobile_no', models.CharField(max_length=15)),
                ('student_id_no', models.CharField(max_length=15)),
                ('student_image', models.ImageField(upload_to='stu_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_first_name', models.CharField(max_length=20)),
                ('teacher_middle_name', models.CharField(max_length=20)),
                ('teacher_last_name', models.CharField(max_length=20)),
                ('teacher_username', models.CharField(max_length=100)),
                ('teacher_dob', models.DateTimeField(verbose_name='date published')),
                ('teacher_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('teacher_address', models.CharField(max_length=200)),
                ('teacher_address2', models.CharField(default='NO_ADDR', max_length=200)),
                ('teacher_city', models.CharField(max_length=20)),
                ('teacher_state', models.CharField(max_length=20)),
                ('teacher_zip', models.CharField(max_length=7)),
                ('teacher_mobile_no', models.CharField(max_length=15)),
                ('teacher_id_no', models.CharField(max_length=15)),
                ('teacher_image', models.ImageField(upload_to='teacher_pics')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.CharField(max_length=50)),
                ('c_id', models.CharField(max_length=10)),
            ],
            options={
                'unique_together': {('student_email', 'c_id')},
            },
        ),
    ]