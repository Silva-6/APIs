from django.db import models

# Create your models here.
class Rating(models.Model):
    menuitem_id = models.SmallIntegerField()
    rating = models.aggregatesSmallIntegerField()
    category = models.ForeignKey(User, on_delete=models.CASCADE)
