"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from about.views import my_about
from blog.views import my_blog
from contact.views import my_contact
from projects.views import my_projects
from reviews.views import my_reviews

urlpatterns = [
    path('about', my_about, name='about'),
    path('blog/', my_blog, name='blog'),
    path('contact/', my_contact, name='contact'),
    path('projects/', my_projects, name='projects'),
    path('reviews/', my_reviews, name='reviews'),
    path('admin/', admin.site.urls),
]
