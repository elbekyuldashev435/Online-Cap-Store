from django.contrib import admin
from .models import Categories, Caps, Colors, Sizes, Review
# Register your models here.

admin.site.register(Categories)
admin.site.register(Sizes)
admin.site.register(Caps)
admin.site.register(Colors)
admin.site.register(Review)