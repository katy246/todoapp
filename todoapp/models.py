import uuid
from datetime import date

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Task(models.Model):
    title = models.CharField(max_length=300)

    due_date = models.DateField(blank=True, validators=[MinValueValidator(limit_value=date.today)])

    description = models.TextField(max_length=1000, help_text='Enter a brief description of the task', blank=True)

    PRIORITIES = (
        ('h', 'High'),
        ('l', 'Low'),
        ('m', 'Medium'),
    )

    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
        blank=True,
        default='m',
        help_text='Task Priority',
    )
    OPTIONS = (
        ('0', 'Not Started'),
        ('wip', 'Work In Progress'),
        ('1', 'Done'),
        ('wait', "Waiting on")
    )

    status = models.CharField(
        max_length=4,
        choices=OPTIONS,
        blank=True,
        default='0',
        help_text='Task Status',
    )

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
