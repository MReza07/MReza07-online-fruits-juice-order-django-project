from django.db import models


class contact_info(models.Model):
    cname = models.CharField(max_length=50, blank=False)
    cemail = models.EmailField()
    csubject = models.CharField(max_length=50, blank=False)
    cmessage = models.TextField()

    def __str__(self):
        return self.cname


