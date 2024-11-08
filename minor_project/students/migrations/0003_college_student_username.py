# Generated by Django 5.1.2 on 2024-11-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_delete_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=50)),
                ('college_type', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
