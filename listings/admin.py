from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # Determines which links in the diplay actually go to the item
    list_filter = ('realtor',) # Adds filter box to filter items by a certain field.
    list_editable = ('is_published',) # Makes certain fields editable from display
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') # Means you're able to search for different items by certain fields
    list_per_page = 25 # Determines how many items are shown on each page

# Register your models here.
admin.site.register(Listing, ListingAdmin)