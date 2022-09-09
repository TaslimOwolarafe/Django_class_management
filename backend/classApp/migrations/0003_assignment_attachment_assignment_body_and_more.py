# Generated by Django 4.0.7 on 2022-09-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0002_remove_announcement_teacher_announcement_teacher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='attachment',
            field=models.FileField(null=True, upload_to='assignments/'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='body',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='assignmentsolution',
            name='solution',
            field=models.FileField(upload_to='assignments_solutions/'),
        ),
    ]
