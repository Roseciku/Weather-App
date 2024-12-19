import urllib.request #helps to access APIs and send requests and accept responses
import json 
from django.shortcuts import render 
from dotenv import load_dotenv
import os
# Create your views here.
# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
# API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

def index(request):

    if request.method == 'POST':
        city = request.POST['city']
        API_KEY = os.getenv('OPEN_WEATHER_API_KEY')

        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)


    