from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,default='SOME STRING')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=300,default='product')
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)



    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id.id
        }