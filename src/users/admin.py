from django.contrib import admin
from .models import Profile, location

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'bio', 'phone_number')
    search_fields = ('user__username', 'bio', 'phone_number')
    list_filter = ('user__is_active',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('address_1', 'address_2', 'city', 'state', 'zip_code')
    search_fields = ('address_1', 'address_2', 'city', 'state', 'zip_code')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(location, LocationAdmin)