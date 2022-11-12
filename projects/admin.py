from django.contrib import admin
from projects.models import Dice, Image

class DiceAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dice, DiceAdmin)
admin.site.register(Image, ImageAdmin)
