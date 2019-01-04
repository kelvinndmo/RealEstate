from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','is_published','title','realtor','price')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','adress','county',)   
# Register your models here.
admin.site.register(Listing, ListingAdmin)
