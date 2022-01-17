from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    print(request.user)
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def sell(request):
    return render(request, 'sell.html')

def communities(request):
    return render(request, 'communities.html')

def properties(request):
    return render(request, 'properties.html')

def listings(request):
    return render(request, 'listings.html')

def resources(request):
    return render(request, 'resources.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'