from django.shortcuts import render

from django.http import HttpResponse

from listings.models import Listing

from listings.choices import bedroom_choices,price_choices,state_choices

from realtors.models import Realtor

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices,
        
    }
    return render(request, 'pages/index.html', context)

def about(request):
    #Get all realtors

    realtors = Realtor.objects.order_by('-hire_date')[:3]

    #Get is mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request, 'pages/about.html', context)
