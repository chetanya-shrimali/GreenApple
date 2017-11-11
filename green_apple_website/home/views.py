from django.http import HttpResponse
from django.shortcuts import render
# import twilio
# import twilio.rest
import json


# from urllib.request import urlopen


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
    # put your own credentials here
    account_sid = "ACaf877765944a5bd7a55c53011d66ce1e"  # your sid here
    auth_token = "636da8b8dbadffe6e66beb6359f3e313"  # auth token from twilio
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(
        to="+918233813183",
        from_="+12283258038",
        body="Hey!! Its twilio!!",
        media_url="https://climacons.herokuapp.com/clear.png")

    print('done')
    return HttpResponse("Message API")
