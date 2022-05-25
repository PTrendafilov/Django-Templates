from django.db import models

# Create your models here.
class Task(models.Model):
    task_text = models.CharField(max_length=200)
    is_finished = models.BooleanField(default=False)
    deadline = models.DateField()
