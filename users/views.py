# views.py
from django.shortcuts import render, redirect, HttpResponse
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ticket.models import Ticket, FlightInfo
# from qr_code.qrcode.utils import QRCodeOptions



@login_required
def profile(request):
    customer = request.user
    if str(Ticket.objects.filter(customer=customer)) == '<QuerySet []>':
        messages.warning(request, 'You do not have any Tickets, Please Purchase!')
        return redirect('dashboard')
    tickets = Ticket.objects.filter(customer=customer)
    first_name = customer.first_name
    last_name = customer.last_name
    national_id = customer.national_id
    data = []
    for ticket in tickets:
        data.append([ticket.ticket_ID,ticket.seat_number,
                     ticket.booking_status,ticket.booking_date,
                     ticket.flight_class,ticket.fligh_ID,
                     ticket.QRCODE,ticket.customer])
        
    name = str(first_name).capitalize()+" " +str(last_name).capitalize()
    QRCODE = str(data[0][6])
    flight_ID = str(data[0][5])
    flight_class = str(data[0][4]).upper()
    booking_date = str(data[0][3])
    booking_status = str(data[0][2])
    seat_number = str(data[0][1])
    ticket_id = str(data[0][0])

    flight = FlightInfo.objects.get(Flight_ID = flight_ID)
    arrival = flight.arrival_location
    departure = flight.departure_location


    context = {'name':name,'QRCODE':QRCODE,
               'flight_ID':flight_ID,'flight_class':flight_class,
               'booking_date':booking_date,'booking_status':booking_status,
               'seat_number':seat_number,'ticket_id':ticket_id, 'national_id':national_id,
               'arrival':arrival, 'departure':departure}
    
    return render(request, 'users/profile.html',context)

def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            messages.success(request, 'account created!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# login page
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)   
                messages.success(request,'Logged In! Welcome:)')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Username or Password is/are Incorrect :(')
                return redirect('login')
            
    else:
        form = LoginForm()
    return render(request, 'users/signin.html', {'form': form})

# logout page
def signout(request):
    logout(request)
    messages.info(request, 'Logged Out!!!')
    return redirect('home')

