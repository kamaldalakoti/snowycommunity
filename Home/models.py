from django.db import models

# Create your models here.
class signup(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=30)
    PubgID = models.TextField(max_length=20  )
    City = models.TextField(max_length=110  )
    District = models.TextField(max_length=110  )
    State = models.TextField(max_length=110  )
    Pic = models.FileField(upload_to="static", storage=None)
    def __str__(self):
        return self.Name    