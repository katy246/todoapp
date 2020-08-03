# Generated by Django 3.0.8 on 2020-08-01 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(help_text='Enter a brief description of the task', max_length=1000)),
                ('priority', models.CharField(blank=True, choices=[('h', 'High'), ('l', 'Low'), ('m', 'Medium')], default='m', help_text='Task Priority', max_length=1)),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
