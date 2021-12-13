from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(null=True, upload_to='images/', blank=True)

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

    knows = models.ManyToManyField(Subject, related_name='knows_subjects', blank=True)
    learns = models.ManyToManyField(Subject, related_name='learns_subjects', blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def profile_photo(self):
        return self.image or 'images/default-user.png'

    def short_description(self):
        if self.description:
            return self.description[0:800]


class Comment(models.Model):
    for_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=280, verbose_name='Your comment')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
