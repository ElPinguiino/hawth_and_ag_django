from django.urls import path
from backendsite import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
        path('', views.index, name="index"),
        path('search', views.search, name="search"),
        path('sell', views.sell, name="sell"),
        path('communities', views.communities, name="communities"),
        path('properties', views.properties, name="properties"),
        path('listings', views.listings, name="listings"),
        path('resources', views.resources, name="resources"),
        path('about', views.about, name="about"),
        path('contact', views.contact, name="contact"),
        path('signup', views.signup, name="signup"),

        path('accounts/profile', views.ProfileView.as_view(), name="profile"),


        #Django Auth
        path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
        path('accounts/logout', auth_views.LogoutView.as_view(), name="logout")
]
