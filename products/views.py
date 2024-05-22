from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView
from .models import Categories, Caps, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddReviewForm
# Create your views here.


class CategoryListView(View):
    def get(self, request):
        categories = Categories.objects.all()
        context = {
            'form': categories
        }
        return render(request, 'category_list.html', context=context)


class MaleListView(View):
    def get(self, request, pk):
        caps = Caps.objects.filter(category_name=pk).order_by('-id')
        context = {
            'male_caps': caps
        }
        return render(request, 'male_list.html', context=context)


class MaleDetailView(View):
    def get(self, request, pk):
        caps = Caps.objects.get(pk=pk)
        context = {
            'cap': caps,
        }
        return render(request, 'detail.html', context=context)


class FemaleListView(View):
    def get(self, request, pk):
        caps = Caps.objects.filter(category_name=pk).order_by('-id')
        context = {
            'female_caps': caps
        }
        return render(request, 'female_list.html', context=context)


class CapCreateView(CreateView):
    model = Caps
    template_name = 'create_caps.html'
    fields = '__all__'
    success_url = reverse_lazy('products:category-list')


class BookDeleteView(DeleteView):
    model = Caps
    template_name = 'delete_caps.html'
    success_url = reverse_lazy('products:category-list')


class AddReview(LoginRequiredMixin, View):
    def get(self, request, pk):
        caps = Caps.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'caps': caps,
            'add_review_form': add_review_form
        }
        return render(request, 'add_review.html', context=context)

    def post(self, request, pk):
        caps = Caps.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            # Ensure user is authenticated
            if request.user.is_authenticated:
                review = Review.objects.create(
                    comment=add_review_form.cleaned_data['comment'],
                    book=caps,
                    user=request.user,
                    star_given=add_review_form.cleaned_data['star_given']
                )
                review.save()
                return redirect('products:category-list')
            else:
                # Handle the case where user is not authenticated
                return redirect('login')  # Redirect to login page
        else:
            context = {
                'caps': caps,
                'add_review_form': add_review_form
            }
            return render(request, 'add_review.html', context=context)


class SaveCapView(View):
    def get(self, request, pk):
        caps = Caps.objects.get(pk=pk)
        context = {
            'caps': caps
        }
        return render(request, 'save_cap.html', context=context)