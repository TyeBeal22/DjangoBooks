from django.db import models

class Paragraph(models.Model):
    name = models.TextField(default="-")
    pt = models.TextField(default="-")
    p2 = models.TextField(default="-")
    p3 = models.TextField(default="-")
    p4 = models.TextField(default="-")

    def __str__(self):
        return self.name
