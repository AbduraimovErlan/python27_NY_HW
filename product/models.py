from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def products_count(self):
        return self.product_set.count()

    def products_list(self):
        return [product.title for product in self.product_set.all()]

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def reviews(self):
        return self.review_set.all()

    @property
    def category_name(self):
        return self.category.name if self.category else ""

    @property
    def rating(self):
        stars_list = [review.stars for review in self.reviews]
        return round(sum(stars_list) / len(stars_list), 2) if stars_list else 0



STAR_CHOICES = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
)
class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES, null=True)


    def __str__(self):
        return self.text

    @property
    def product_name(self):
        return self.product.title if self.product else ""



