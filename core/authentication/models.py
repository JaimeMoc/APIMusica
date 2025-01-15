from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    class Meta:
        ordering = ['-id']
        
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=50, null = True, blank = True)
    email = models.EmailField(max_length=130, unique = True, null = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - UUID: {self.uuid}"
