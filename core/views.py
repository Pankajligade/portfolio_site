from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.



def home(request):
    return render(request,'core/home.html')


def contact(request):
    return render(request,'core/contact.html')

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        requirements = request.POST.get('requirements')

        # Create an instance of the Contact model
        contact = Contact(name=name, email=email, requirements=requirements)
        contact.save()  # Save the instance to the database

        # Return a success message
        success_message = '<div class="alert alert-success"><i class="fa-solid fa-thumbs-up mr-2"></i> Form submitted successfully</div>'
        return HttpResponse(success_message)
    else:
        return HttpResponse('Method not allowed')