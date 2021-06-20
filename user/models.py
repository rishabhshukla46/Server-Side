from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  userId = models.CharField(max_length=100, primary_key=True)
  EMAIL = 'email'
  PHONE = 'phone'
  PREFERENCE_CHOICES = [
    (EMAIL, 'email'),
    (PHONE, 'phone')
  ]
  notify = models.CharField(
    max_length=10,
    choices=PREFERENCE_CHOICES,
    default=EMAIL,
  )

  def __str__ (self):
    return self.name 

