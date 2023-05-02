from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()
    descriotion = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(null=True)

    def __str__(self):
        return self.title
