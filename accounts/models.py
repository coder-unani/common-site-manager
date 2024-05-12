from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=20, null=True)
    grade = models.CharField(max_length=10, null=True)
    profile_image = models.CharField(max_length=100, null=True)
    token = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nickname
    
    class Meta:
        db_table = "accounts"