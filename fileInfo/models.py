from django.db import models

# Create your models here.
class file_info(models.Model):
    file_name = models.CharField(max_length=20)
    file_id = models.CharField(max_length=20)
    file_user = models.CharField(max_length=20)