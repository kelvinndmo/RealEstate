from django.shortcuts import render,redirect

from django.contrib import messages

from django.core.mail import send_mail

from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check if user has made iquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry on this listing')
                return redirect('/listings/' + listing_id)


            contact = Contact(listing=listing,email=email,message=message,phone=phone,user_id=user_id,listing_id=listing_id, name=name)

            contact.save()

            send_mail(
                'Millicent Kerubo properties',
                'We will normally just iterate it like any other Iterable: using a for-loop. However, given non-trivial conditions for the end of the loop, or for its continuation, we may end up in a situation where we’d like to iterate it manually. To do this, we will just call the next method (Python 2) or function (Python 3) until it throws a StopIteration exception. Note that the time taken for generating each element individually on retrieval will end up adding up to take as much as the time for initializing the whole list in a non-lazy manner. Finally, given a Generator, we can always cast it into a plain old non-lazy list by calling list(our_generator), paying the whole initialization cost.',
                'ndemo.kelvin@students.jkuat.ac.ke',
                [realtor_email, 'ndemokelvinonkundi@gmail.com','ndemokelvin254@gmail.com','onkundipol@yahoo.com'],
                fail_silently=True
            )

            messages.success(request, "Your form has been submitted and a realtor will get back to you!!")

            return redirect('/listings/' + listing_id)
        
        return redirect('/listings/' + listing_id)
    
        
