from django.core.exceptions import ValidationError
from django.test import TestCase

from django.test import TestCase

from todoapp.models import Task


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='Task one', description='Long list of stuff to do ')

    def test_title_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEquals(max_length, 300)

    def test_invalid_due_date_fails(self):  # todo claims validation error is not raised #fix
        with self.assertRaises(ValidationError):
            Task.objects.create(title='Task one', description='Long list of stuff to do', due_date='2019-08-01')
