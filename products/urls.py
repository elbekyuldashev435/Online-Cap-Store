from django.urls import path
from .views import CategoryListView, MaleListView, FemaleListView, MaleDetailView, CapCreateView, BookDeleteView, \
    AddReview, SaveCapView

app_name = 'products'
urlpatterns = [
    path('category-list/', CategoryListView.as_view(), name='category-list'),
    path('products/<int:pk>/', MaleListView.as_view(), name='male-list'),
    path('products/<int:pk>/', FemaleListView.as_view(), name='female-list'),
    path('products/detail/<int:pk>/', MaleDetailView.as_view(), name='detail'),
    path('products/create', CapCreateView.as_view(), name='create-cap'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete-cap'),
    path('add-review/<int:pk>', AddReview.as_view(), name='add-review'),
    path('save/<int:pk>/', SaveCapView.as_view(), name='save-cap'),
]