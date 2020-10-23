import random
import json
import requests
from django.utils.text import slugify
from .models import Vendor, Category, LiveGame, SlotGame


def get_random_name():
    alphanum = ['a' ,'b', 'c', 'd', 'e', 'x', 'y', 'z' , '0', '1', '2',
                'f', 'g', '3', '4', '5', '6', '7', '8', '9']
    name = ''
    for i in range(10):
        name += random.choice(alphanum)
    return name


def create_new_game(game_type):
    vendors = Vendor.objects.all()
    categories = Category.objects.all()
    number_of_choices = random.randint(1, len(categories))
    name = 'Game Test ' + get_random_name(),
    game_categories = random.sample(list(categories), number_of_choices)
    params = {
    'name': name,
    'slug': slugify(name),    
    'vendor': random.choice(list(vendors)),      
    }
    
    if game_type:
        params['dealer_gender'] = random.choice(['M', 'F'])
        params['dealer_language'] = random.choice(['EN', 'RO', 'FR', 'DE'])
        live_game = LiveGame(**params)        
        live_game.save()
        live_game.categories.set(game_categories)
    else:
        params['jackpot_currency'] = random.choice(['USD', 'EUR'])
        params['jackpot'] = random.randint(100, 10000)
        slot_game = SlotGame(**params)        
        slot_game.save()
        slot_game.categories.set(game_categories)
    

def generate_fake_names(item):
    if item == 'vendor':
        alt = 'Vendor '
    elif item == 'category':
        alt = 'Category '
    else:
        pass
    name = "Fake " + alt + get_random_name()
    slug = slugify(name)
    params = {
        'name': name,
        'slug': slug
    }
    return json.dumps(params)

# def simulate_api_call(endpoint, params):
#     final_endpoint = 'http://localhost:8000/' + endpoint + '/' + \
#         params[0] + '/' + params[1] + '/'
#     print(final_endpoint)
#     res = requests.get(final_endpoint)
#     return res.json()

