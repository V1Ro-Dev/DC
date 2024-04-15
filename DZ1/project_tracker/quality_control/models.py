from django.db import models
from tasks.models import Project, Task

class Bugreport(models.Model):
    STATUS_LIST = [
        ("New", "Новый"),
        ("Processing...", "В работе..."),
        ("Completed", "Завершена")
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_LIST,
        default="New"
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_LIST = [
        ("On review", "На рассмотрении"),
        ("Completed", "Завершена"),
        ("Отклонена", "Declined")
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_LIST,
        default="On review"
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
