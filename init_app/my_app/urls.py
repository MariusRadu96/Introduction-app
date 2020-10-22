from django.urls import path
from .views import *

app_name = 'myapp'
urlpatterns = [
    path('game_categories/<slug>/<game_type>/', game_categories, name='game_categories'),
    path('game_vendors/<slug>/<game_type>/', game_vendors, name='game_vendors'),
    path('games_by_vendor/<vendor_slug>/', games_by_vendor, name='games_by_vendor'),
]