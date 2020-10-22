from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .serializers import *
from .models import *


@api_view(['GET', 'POST'])
def game_categories(request, slug, game_type):
    game_type = game_type.lower()
    if game_type == 'live':
        try:
            game = LiveGame.objects.get(slug=slug)
        except LiveGame.DoesNotExist:
            content = {'error': 'No such object.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif game_type == 'slot':
        try:
            game = SlotGame.objects.get(slug=slug)
        except SlotGame.DoesNotExist:
            content = {'error': 'No such object.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    else:
        data_out = {}
        data_out['error']: "Please specify the game type(live or slot)."
        return Response(data_out)

    if request.method == 'GET':
        categories = game.categories.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    else:
        category_slug = request.POST['category_slug']
        try:
            category = Category.objects.get(slug=category_slug)
            game.categories.add(category)
            game.save()
            data_out = {}
            data_out['response'] = (f'Successfully added the new ' 
                'category {category.name} to the game {game.name}.')
            return Response(data_out)

        except Category.DoesNotExist:
            content = {'error': 'No such object.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET', 'POST'])
def game_vendors(request, slug, game_type):
    game_type = game_type.lower()

    if game_type == 'live':
        try:
            game = LiveGame.objects.get(slug=slug)
        except LiveGame.DoesNotExist:
            content = {'error': 'No such object.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    elif game_type == 'slot':
        try:
            game = SlotGame.objects.get(slug=slug)
        except SlotGame.DoesNotExist:
            content = {'error': 'No such object.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

    else:
        data_out = {}
        data_out['error']: "Please specify the game type(live or slot)."
        return Response(data_out)
    
    if request.method == 'GET':
        vendor = game.vendor
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    else:
        vendor_slug = request.POST['vendor_slug']
        try:
            vendor = Vendor.objects.get(slug=vendor_slug)
            game.vendor = vendor
            game.save()
            data_out = {}
            data_out['response'] = (f'Successfully added the game ' 
                '{game.name} to the vendor {vendor.name}.')
            return Response(data_out)

        except Vendor.DoesNotExist:
            content = {'error': 'No such object.'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
def games_by_vendor(request, vendor_slug):
    try:
        vendor = Vendor.objects.get(slug=vendor_slug)
    except Vendor.DoesNotExist:
        content = {'error': 'No such object.'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        live_games = vendor.livegame_set.all()
        slot_games = vendor.slotgame_set.all()
        live_games_serializer = LiveGameSerializer(live_games, many=True)
        slot_games_serializer = SlotGameSerializer(slot_games, many=True)
        response = live_games_serializer.data + slot_games_serializer.data
        return Response(response)
        


