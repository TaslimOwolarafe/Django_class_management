# Generated by Django 4.0.7 on 2022-09-09 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='teacher',
        ),
        migrations.AddField(
            model_name='announcement',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='announcements', to='classApp.teacher'),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='student_class',
        ),
        migrations.AddField(
            model_name='assignment',
            name='student_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', to='classApp.studentclass'),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='teacher',
        ),
        migrations.AddField(
            model_name='assignment',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assignments', to='classApp.teacher'),
        ),
    ]
