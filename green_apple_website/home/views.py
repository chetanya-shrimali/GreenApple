import json
from urllib.request import urlopen

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def maps_api(request):
    origin = ''
    destination = ''
    query = "https://maps.googleapis.com/maps/api/distancematrix/json?units" \
            "=imperial&origins=Washington,DC&destinations=New+York+City," \
            "" \
            "NY&key=AIzaSyAhECZTm_lnmPZPf3LVxytigP7C6NxWfoQ"
    # print(query)
    connection = urlopen(query)
    # print(connection)
    output = connection.read()
    # print(output)
    json_output = json.loads(output)
    # print(json_output)
    final_distance = json_output["rows"][0]["elements"][0]['distance']['value']
    print(final_distance)
    return HttpResponse(json.dumps(json_output),
                        content_type="application/json")


def message_api(request):
    return HttpResponse("Message API")
