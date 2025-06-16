from django.db import models

# Create your models here.
class TaskStatus(models.IntegerChoices):
    PENDING = 0, 'Pending'
    IN_PROGRESS = 1, 'In Progress'
    COMPLETED = 2, 'Completed'

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(choices=TaskStatus.choices, default=TaskStatus.PENDING)
    due_date = models.DateTimeField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    responsible = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-due_date']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'