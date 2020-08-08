from django.db import models

# Create your models here.
class signup(models.Model):
    Name = models.CharField(max_length=20)
    Phone = models.CharField(max_length=30)
    # gen = models.ChoicesField()
    # PubgID = models.TextField(max_length=20  )
    # whats = models.TextField(max_length=20  )
    City = models.TextField(max_length=20  )
    District = models.TextField(max_length=20  )
    State = models.TextField(max_length=20  )
    # Pic = models.FileField(upload_to="static", storage=None)
    def __str__(self):
        return self.Name    

class news(models.Model):
    T1 = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    Cat = models.CharField(max_length=20)
    Disc = models.CharField(max_length=2000)
    def __str__(self):
        return self.T1    
