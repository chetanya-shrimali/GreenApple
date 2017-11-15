from django.http import HttpResponse
from django.shortcuts import render
import json
from django.apps import apps
import requests


def index(request):
    menu_model = apps.get_model('menu.Menu')
    menu_items = menu_model.objects.all().order_by('id')[:5]
    return render(request, 'home/index.html', {'menu_items': menu_items})


def maps_api(request):
    origin = ''
    destination = ''
    query = "https://maps.googleapis.com/maps/api/distancematrix/json?units" \
            "=metric&origins=Washington,DC&destinations=New+York+City," \
            "" \
            "NY&key=AIzaSyAhECZTm_lnmPZPf3LVxytigP7C6NxWfoQ"
    # print(query)
    connection = requests.get(query)
    # print(connection)
    output = connection.json()
    # print(output)
    final_distance = output["rows"][0]["elements"][0]['distance']['value']
    final_distance_km = output["rows"][0]["elements"][0]['distance']['text']
    print(str(final_distance) + " -> " + final_distance_km)
    return HttpResponse(json.dumps(output),
                        content_type="application/json")

# def message_api(request):
#     # put your own credentials here
#     account_sid = "ACaf877765944a5bd7a55c53011d66ce1e"  # your sid here
#     auth_token = "636da8b8dbadffe6e66beb6359f3e313"  # auth token from twilio
#     client = twilio.rest.Client(account_sid, auth_token)
#     client.messages.create(
#         to="+918233813183",
#         from_="+12283258038",
#         body="Hey!! Its twilio!!",
#         media_url="https://climacons.herokuapp.com/clear.png")
# 
#     print('done')
#     return HttpResponse("Message API")
