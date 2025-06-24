from django.shortcuts import render
from django.views.generic import CreateView
from .models import Booking

# Create your views here.

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

class BookingCreateView(CreateView):
    model = Booking
    fields = ['walk', 'owner', 'dog_size']
    template_name = 'bookings/booking_form.html'
    success_url = '/bookings/'

    def form_valid(self, form):
        # Additional logic can be added here if needed
        return super().form_valid(form)