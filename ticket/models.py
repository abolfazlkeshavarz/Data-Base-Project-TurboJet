from django.db import models
from users.models import CustomUser
class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    contact_info = models.TextField(max_length=200)
    airline_ID = models.CharField(max_length=50)
    partnary = models.ManyToManyField('Airport', through='Partner', blank=True)
    def __str__(self):
        return self.airline_name

class Airport(models.Model):
    IATA_CODE = models.CharField(max_length=50)
    airport_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    partnary = models.ManyToManyField('Airline', through='Partner', blank=True)
    def __str__(self):
        return self.airport_name

class Partner(models.Model):
    airline_ID = models.ForeignKey(Airline,on_delete= models.CASCADE)
    airport_ID = models.ForeignKey(Airport, on_delete=models.CASCADE)
    paid_partner = models.BooleanField(default=True)


class Aircraft(models.Model):
    CHOICES = (('boeing', 'Boeing'),
                ('air bus', 'Air Bus'),
                ('bombardier', 'Bombardier'),
                ('lockheed martin', 'Lockheed Martin'),
                ('gulf stream', 'Gulf Stream'))
    aircraft_model = models.CharField(max_length= 50)
    plane_ID = models.CharField(max_length=100)
    seating_capacity = models.IntegerField()
    manufacturer = models.CharField(max_length=100, choices = CHOICES)
    airline_name = models.ForeignKey(Airline, on_delete=models.CASCADE)
    def __str__(self):
        return self.aircraft_model

class FlightInfo(models.Model):
    CHOICES = (('business', 'Business'),
               ('economy', 'Economy'),
               ('vip', 'VIP'))
    
    Flight_ID = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    departure_location = models.CharField(max_length = 100)
    arrival_location = models.CharField(max_length = 100)
    flight_type = models.CharField(max_length = 100, choices=CHOICES)
    plane_ID = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return self.Flight_ID

class Payment(models.Model):
    transaction_ID = models.CharField(max_length=100)
    Price = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return self.transaction_ID

class Ticket(models.Model):
    CHOICES = (('class a', 'CLASS A'), ('class b', 'CLASS B'), ('class c', 'CLASS C'))
    ticket_ID = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=100)
    booking_status = models.OneToOneField(Payment,on_delete= models.CASCADE)
    booking_date = models.DateField()
    flight_class = models.CharField(max_length= 100, choices=CHOICES)
    fligh_ID = models.ForeignKey(FlightInfo, on_delete=models.CASCADE)
    QRCODE = models.CharField(max_length= 100)
    customer = models.ForeignKey(CustomUser, on_delete= models.CASCADE)

    def __str__(self):
        return self.ticket_ID
