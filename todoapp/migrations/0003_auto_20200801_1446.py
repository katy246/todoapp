# Generated by Django 3.0.8 on 2020-08-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, help_text='Enter a brief description of the task', max_length=1000),
        ),
    ]