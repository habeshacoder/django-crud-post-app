from django.db import models


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id,self.title, self.content,self.created}"
