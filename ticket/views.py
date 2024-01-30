from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import QueryForm
from .models import FlightInfo, Ticket, Payment
from users.models import CustomUser
import random, string
from datetime import date
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'ticket/home.html',{'user':request.user})


def search(request):
    if request.method == 'GET':
        form = QueryForm(request.GET)
        if form.is_valid():
            from_location = form.cleaned_data['from_location']
            to_location = form.cleaned_data['to_location']
            date = form.cleaned_data['date']
             
            results = FlightInfo.objects.filter(departure_location=from_location,arrival_location=to_location,departure_date= date)
            data = []
            for result in results:
                data.append([result.Flight_ID,result.departure_date,result.departure_time,result.arrival_date,result.departure_location,result.arrival_location,result.flight_type,result.plane_ID])
            context = []
            for item in data:
                flight_info = {
                    'flight_id': item[0],
                    'departure_date': item[1],
                    'departure_time': item[2],
                    'arrival_date': item[3],
                    'departure_location': item[4],
                    'arrival_location': item[5],
                    'flight_type': item[6],
                    'plane_id': item[7],
                }
                context.append(flight_info)
                    
            return render(request,'ticket/search_result.html',{'data':context})

    else:
        form = QueryForm()
    return render(request, 'ticket/search.html', {'form': form})    

@login_required
def flights(request):
    results = FlightInfo.objects.all()
    data = []
    for result in results:
        data.append([result.Flight_ID,result.departure_date,result.departure_time,result.arrival_date,result.departure_location,result.arrival_location,result.flight_type,result.plane_ID])
    context = []
    for item in data:
        flight_info = {
            'flight_id': item[0],
            'departure_date': item[1],
            'departure_time': item[2],
            'arrival_date': item[3],
            'departure_location': item[4],
            'arrival_location': item[5],
            'flight_type': item[6],
            'plane_id': item[7],
        }
        context.append(flight_info)    
    return render(request, 'ticket/flights.html',{'flights':context})

def buy(request):
    # flight_id = request.GET.get('flight_id')
    # flight = FlightInfo.objects.get(Flight_ID = flight_id)
    customer = request.user
    usere = CustomUser.objects.get(username=customer)
    if str(Ticket.objects.filter(customer= usere)) == '<QuerySet []>':
        flight_id = request.GET.get('flight_id')
        flight = FlightInfo.objects.get(Flight_ID = flight_id)
        seat_number = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=2))
        payment = Payment.objects.create(transaction_ID=''.join(random.choices('0123456789', k=12)),Price = 1000, status= True)
        ticket = Ticket.objects.create(
            ticket_ID = ''.join(random.choices('0123456789', k=12)),
            seat_number=seat_number,
            fligh_ID=flight,
            booking_status = payment,
            booking_date = date.today(),
            flight_class = 'CLASS A',
            QRCODE = ''.join(random.choices('0123456789', k=12)),
            customer= customer)
        context ={
            'flight_id':flight_id,
            'customer_first': customer.first_name,
            'customer_last' : customer.last_name,
            'seat_number' : seat_number,
            'departure_date': flight.departure_date,

        }
        messages.info(request, 'Ticket Purchased!')
        return render(request, 'ticket/buy.html', context)
    else:
        messages.warning(request, 'You Have Ticket :)')
        return redirect("profile")


def whyus(request):
    return render(request, 'ticket/whytj.html')

def about(request):
    return render(request, 'ticket/about.html')