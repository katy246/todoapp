# Generated by Django 3.0.8 on 2020-08-01 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'Not Started'), ('wip', 'Work In Progress'), ('1', 'Done'), ('wait', 'Waiting on')], default='0', help_text='Task Status', max_length=4),
        ),
    ]
