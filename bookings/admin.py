from django.contrib import admin
from .models import Walk, Booking, Review

# Register your models here.

class WalkAdmin(admin.ModelAdmin):
    list_display = ('walker', 'date', 'time_of_day', 'number_of_dogs', 'address', 'created_at')
    search_fields = ('walker__username', 'date', 'time_of_day', 'address')
    list_filter = ('date', 'time_of_day', 'walker')




admin.site.register(Walk, WalkAdmin)
admin.site.register(Booking)
admin.site.register(Review)
