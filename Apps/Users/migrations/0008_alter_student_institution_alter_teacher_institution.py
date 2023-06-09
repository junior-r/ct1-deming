# Generated by Django 4.2.1 on 2023-06-14 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_alter_teacher_institution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.institution', verbose_name='students'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.institution', verbose_name='teachers'),
        ),
    ]
