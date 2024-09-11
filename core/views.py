from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.



def home(request):
    return render(request,'core/home.html')


def contact(request):
    return render(request,'core/contact.html')



from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import Contact

def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        requirements = request.POST.get('requirements')
        
        # Save the form data to the database
        contact = Contact(name=name, email=email, requirements=requirements)
        contact.save()

        # Send email
        subject = 'New Contact Us Submission'
        message = f'Name: {name}\nEmail: {email}\nRequirements: {requirements}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['recipient-email@example.com']  # Add the email where you want to receive the contact form info
        
        try:
            send_mail(subject, message, from_email, recipient_list)
            success_message = '<div class="alert alert-success"><i class="fa-solid fa-thumbs-up mr-2"></i> Form submitted successfully and email sent.</div>'
        except Exception as e:
            print(e)
            success_message = '<div class="alert alert-warning"><i class="fa-solid fa-thumbs-down mr-2"></i> Form submitted, but email failed to send.</div>'
        
        return HttpResponse(success_message)
    else:
        return HttpResponse('Method not allowed')



# def contact_submit(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         requirements = request.POST.get('requirements')
#         # Create an instance of the Contact model
#         contact = Contact(name=name, email=email, requirements=requirements)
#         contact.save()  # Save the instance to the database

#         # Return a success message
#         success_message = '<div class="alert alert-success"><i class="fa-solid fa-thumbs-up mr-2"></i> Form submitted successfully</div>'
#         return HttpResponse(success_message)
#     else:
#         return HttpResponse('Method not allowed')   