from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        content = request.POST['content']

        if len(name)<2:
                    messages.error(request, 'Please enter the name which is greater than 2 words')
        elif name == "":
                messages.error(request, 'Please enter your name')
        elif len(email)<4:
                messages.error(request, 'Wrong email address! Please check again')
        elif email!=email:
                messages.error(request, 'Wrong email address! Please check again')
        elif email=="":
                messages.error(request, 'Please enter your email')
        elif subject=="":
                messages.error(request, 'PLease enter your subject')
        elif content=="":
                messages.error(request, 'Please type your message here')
        else:  
            contact = Contact(name=name, email=email, subject=subject, content=content)
            contact.save()
            messages.success(request, 'Your form has been submitted successfully')
    return render(request, 'index.html')
