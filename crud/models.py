from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    name = models.CharField(max_length=150)
    published_year = models.DateField(auto_now=True)
    price = models.IntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)


