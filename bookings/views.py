from django.shortcuts import render
from django.views.generic import CreateView
from .models import Booking
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

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


def google_verification(request):
    return HttpResponse(
    "google-site-verification: google6cC0gzeNqpXBJv51P3XsFicX5dp3y-gFP6o1kYiEqXU.html",
    content_type="text/plain"
)



