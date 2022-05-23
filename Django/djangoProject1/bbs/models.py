from django.db import models

# Create your models here.


class Bbs(models.Model):
    no = models.IntegerField(100)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    writer = models.CharField(max_length=255)

    def __str__(self):
        return str(self.no) + ", " + \
               self.title + ", " + \
               self.content + ", " + \
               self.writer
