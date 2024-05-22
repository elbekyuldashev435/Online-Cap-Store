from django.db import models

# Create your models here.


class About(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True, default='default_img/user_img.png')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.TextField()

    class Meta:
        db_table = 'about_us'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"