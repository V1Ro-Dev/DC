from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='not selected'
    )
    PRIORITY_CHOICES = [
        (1, "low"),
        (2, "medium"),
        (3, "high"),
        (4, "Critical"),
        (5, "immediate fix"),
    ]

    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    STATUS_CHOICES = [
        ("Not Selected", "Не выбрана"),
        ("Processing...", "Рассмотрение"),
        ("Accepted", "Принято"),
        ("Rejected", "Отклонено"),
    ]
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='Not Selected'
    )

    PRIORITY_CHOICES = [
        (1, "low"),
        (2, "medium"),
        (3, "high"),
        (4, "Critical"),
        (5, "immediate fix"),
    ]
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
