from django.db import models

class Insta(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "insta"
    def __str__(self):
        return self.username