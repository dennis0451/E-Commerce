from django.http import HttpResponseRedirect, JsonResponse
from http.client import HTTPResponse
from django.shortcuts import render
import requests as HTTP_Client
import json
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

cart_total = 0

inventory_list = []

pp = pprint.PrettyPrinter(indent=2, depth=2)
print(os.environ)
def index(request):
    item = request.GET.get('wish') or 'fish'

    # public key and private key
    auth = OAuth1(os.environ['apiKey'],
                  os.environ['secretKey'])
    endpoint = f"http://api.thenounproject.com/icon/{item}"

    response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = response.json()
    # pp.pprint(responseJSON['icon']['preview_url'])

    preview_url = responseJSON['icon']['preview_url']
    return render(request, "amzin_app/index.html",{'preview_url':preview_url})


def fitness(request):
    test = 'fitness'
    
    return render(request, "amzin_app/fitness.html",{'test':test})


def martial(request):
    test2 = 'martial arts'

    return render(request, "amzin_app/martial.html", {'test2' : test2})

def aquatics(request):
    test3= 'aquatics'

    return render(request, "amzin_app/aquatics.html", {'test3' : test3})

def cart(request):
    test4= 'give me your money now'

    return render(request, "amzin_app/cart.html", {'test4' : test4})

def checkout(request):
    test6= 'give me your money now'

    return render(request, "amzin_app/checkout.html", {'test6' : test6})


def search(request):
   
    return render(request, "amzin_app/search.html")

def products(request):
   
    query = request.GET.get('query')

    auth = OAuth1(os.environ['apiKey'],
                  os.environ['secretKey'])
    endpoint = f"http://api.thenounproject.com/icon/{query}"
    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = json.loads(API_response.content)
    print(responseJSON['icon']['preview_url'])

    preview_url = responseJSON['icon']['preview_url']

    return JsonResponse({'url':preview_url})
