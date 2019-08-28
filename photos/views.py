from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt



# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def photos_of_day(request):
    date = dt.date.today()
    photos = Image.photos_of_day()
    return render(request, 'all/today_photos.html', {"date": date, "photos":photos})
   
   
   