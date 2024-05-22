
from django.shortcuts import render, redirect, get_object_or_404
from .models import About
from django.views import View
from .forms import AboutViewForm
# Create your views here.


def home_page(request):
    return render(request, 'home.html')


class AboutView(View):
    def get(self, request):
        about1 = About.objects.all()
        context = {
            'about_us': about1
        }
        return render(request, 'about.html', context=context)