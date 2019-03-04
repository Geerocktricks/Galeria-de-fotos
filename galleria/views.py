from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt


# Create your views here.
def welcome(request):
    return HttpResponse('Hello , Welcome to my photo gallery')

def day_today(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)