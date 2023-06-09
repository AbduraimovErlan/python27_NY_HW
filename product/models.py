from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def product_count(self):
        try:
            return self.category.name
        except:
            return None

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title

    @property
    def list_review(self):
        return self.product_rating.all()

    @property
    def category_name(self):
        try:
            return self.category.name
        except:
            return None





STAR_CHOICES = (
    (1, '* '),
    (2, 2 * '* '),
    (3, 3 * '* '),
    (4, 4 * '* '),
    (5, 5 * '* '),
)

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rating')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES, null=True)

    def __str__(self):
        return self.product


    @property
    def product_name(self):

        return self.product.title if self.product.title else ""

    @property
    def count_reviews(self):
        return Review.stars.model.mean

