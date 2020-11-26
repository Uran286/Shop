from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(
        verbose_name='Name of User',
        blank=True, max_length=15
    )

    class Meta:
        permissions = (
            ('can_get_name', 'Can get a name'),

        )

    def __str__(self):
        return f'{self.username}'

