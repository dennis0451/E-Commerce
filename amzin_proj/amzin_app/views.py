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

inventory_list = {
    'items':{
    'instructor': 1000,
    'instructor_pool':5000,
    'instructor_ring':5000,
    'instructor_gym':5000,
    'construction_pool':30000,
    'construction_ring':30000,
    'construction_gym':30000
    },
    'stock':{
    'instructor': 10,
    'instructor_pool':10,
    'instructor_ring':10,
    'instructor_gym':10,
    'construction_pool':10,
    'construction_ring':10,
    'construction_gym':10
    }
}

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
    inventory = inventory_list
    
    return render(request, "amzin_app/fitness.html",{'inventory' :inventory})


def martial(request):
    inventory = inventory_list

    return render(request, "amzin_app/martial.html",{'inventory' :inventory})

def aquatics(request):
    inventory = inventory_list

    return render(request, "amzin_app/aquatics.html", {'inventory' :inventory})

def cart(request):
    inventory = inventory_list

    return render(request, "amzin_app/cart.html",{'inventory' :inventory})

def checkout(request):
    inventory = inventory_list

    return render(request, "amzin_app/checkout.html", {'inventory' :inventory})


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
