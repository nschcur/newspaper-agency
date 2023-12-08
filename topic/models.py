from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def str(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True)

    def str(self):
        return self.username


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publish_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor)

    def str(self):
        return self.title
