from django.db import models
import uuid

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    class Meta:
        ordering = ['-id']
        
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=50, null = True, blank = True)
    email = models.EmailField(max_length=130, unique = True, null = False, blank=False)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Añadir related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Añadir related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - UUID: {self.uuid}"

class ProfileType(models.Model): 
    profile_type = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.profile_type

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    profile_type = models.ForeignKey(ProfileType, on_delete = models.PROTECT)