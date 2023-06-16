# Generated by Django 4.2.1 on 2023-06-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_student_joined_teacher_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]