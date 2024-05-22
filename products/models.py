from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Sizes(models.Model):
    size = models.CharField(max_length=6)

    class Meta:
        db_table = 'sizes'

    def __str__(self):
        return self.size


class Colors(models.Model):
    color = models.CharField(max_length=20)

    class Meta:
        db_table = 'colors'

    def __str__(self):
        return self.color


class Caps(models.Model):
    image = models.ImageField(upload_to='caps/')
    category_name = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.ForeignKey(Colors, on_delete=models.DO_NOTHING)
    price = models.IntegerField()

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'caps'

    def __str(self):
        return f"{self.category_name.name} {self.name}"


class Review(models.Model):
    comment = models.CharField(max_length=200)
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    book = models.ForeignKey(Caps, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f'{self.star_given} - {self.book.name} - {self.user.username}'