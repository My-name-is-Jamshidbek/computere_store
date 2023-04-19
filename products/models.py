from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


# models.py
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model}'


class Photo(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    