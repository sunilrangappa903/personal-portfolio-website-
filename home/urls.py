from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Sunil's Portfolio Admin"
admin.site.site_title = "Sunil's Portfolio Admin Portal" 
admin.site.index_title = "Welcome to Sunil's Portfolio Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
