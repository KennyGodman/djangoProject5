from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datePublished = models.DateTimeField()
    dateUploaded = models.DateTimeField(auto_now=True)
    dateModified = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Author(models.Model):
    firstName = models.CharField(max_length=200)
    lasttName = models.CharField(max_length=200)
    email = models.EmailField
    website = models.URLField


class Publisher(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.firstName


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=5, validators=[MinLengthValidator(5, "code cannot be less than 5"),
                                                         MaxLengthValidator(6, "code cannot exceed a length of 6")])


class BookInstance(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datePublished = models.DateTimeField()
    dateUploaded = models.DateTimeField(auto_now=True)
    dateModified = models.DateTimeField(auto_now_add=True)


#
publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE, primary_key=True)
