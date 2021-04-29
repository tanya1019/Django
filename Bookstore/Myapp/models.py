from django.db import models

# Create your models here.

class BookStore(models.Model):

    def _str_(self):
        return self.name

    name = models.CharField(max_length = 100)
    decs = models.CharField(max_length= 300)
    price = models.IntegerField()
    book_image = models.ImageField(default = 'default.jpg', upload_to = 'book_images/')