from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
class Review(models.Model):
    customer_review = models.TextField()
    
    rating = models.IntegerField()
    
    def __str__(self):
        return self.customer_review
    