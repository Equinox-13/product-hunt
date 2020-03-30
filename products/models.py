from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """
    Implements the attributes of a product
    """
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        """
        Returns a short version of body
        """
        return self.body[:100]

    def pub_date_preety(self):
        """
        Modifies date format
        """
        return self.pub_date.strftime('%b %d %Y')
