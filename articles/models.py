from django.db import models

class Article(models.Model):
    title = models.CharField(max_length= 100)
    slug =  models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)

    def  __str__(self) -> str:
        return self.title

    def summery(self):
        return self.body[:50] + " ..."