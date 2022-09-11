from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:

        ordering = ["status", "-created"]

    def __str__(self):
        return f"{self.content}"


