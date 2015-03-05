from django.db import models
from django.conf import settings
import string
import random

class URL(models.Model):
   url = models.URLField()
   short = models.CharField(max_length=50)
  
   def create_short(self):
      short=''.join(random.choice(string.digits+string.ascii_letters) for i in range(5))
      self.short=short
      return short
     
