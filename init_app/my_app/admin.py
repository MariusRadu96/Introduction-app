from django.contrib import admin
from .models import (
    Game,
    SlotGame,
    LiveGame,
    Vendor,
    Category
)
# Register your models here.

#admin.site.register(Game)
admin.site.register(SlotGame)
admin.site.register(LiveGame)
admin.site.register(Vendor)
admin.site.register(Category)
