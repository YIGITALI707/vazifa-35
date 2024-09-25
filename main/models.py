from django.db import models



class Category(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Movie(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    created_add=models.DateTimeField(auto_created=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.content




class Comment(models.Model):
    author=models.CharField(max_length=50)
    created_add=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Movie,on_delete=models.CASCADE)


    def __str__(self):
        return self.author