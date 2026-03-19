import email

from django.shortcuts import render
from home.models import Contact

# Create your views here.
def index(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'project.html')

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        ns = Contact(name=name, email=email, phone=phone, message=message)
        ns.save()

        print("The data has been written to the database")

    return render(request, 'contact.html')
