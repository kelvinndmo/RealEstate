from django.shortcuts import render,get_object_or_404


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listings.choices import bedroom_choices,price_choices,state_choices

from .models import Listing


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)



    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    
    listing = get_object_or_404(Listing, pk=listing_id)
    
    context = {
    'listing':listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    #town
    if 'town' in request.GET:
        town = request.GET['town']
        if town:
            queryset_list = queryset_list.filter(town__iexact=town)
    
    #county
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county)
    
    #beedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if  bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
        #price
    if 'price' in request.GET:
        price = request.GET['price']
        if  price:
            queryset_list = queryset_list.filter( price__lte=price)
            
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values':request.GET
        
    }
    return render(request, 'listings/search.html', context)