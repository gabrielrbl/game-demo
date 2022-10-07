from django.contrib import admin

from .models import (
    Player,
    PlayerBoard
)

admin.site.register(Player)
admin.site.register(PlayerBoard)
