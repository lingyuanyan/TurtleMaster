from django.db import models

class Corona(models.Model):
    text = models.CharField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.text
class Entry(models.Model):
    topic = models.ForeignKey(Corona, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'

    def _str_(self):
        return self.text[:50] + "..."
