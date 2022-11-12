from django.shortcuts import render
from projects.models import Dice, Image

# Create your views here.
def projects(request):
    dice = Dice.objects.all()[:3]
    images = Image.objects.all()
    context = {
        "dice": dice,
        "images": images
    }
    return render(request, 'index.html', context)

# TODO: Make each page dynamic based on the dice given
def dice_page(request, pk):
    dice = Dice.objects.get(pk=pk)
    images = Image.objects.filter(dice_id=pk)
    context = {
        "dice": dice,
        "images": images
    }
    return render(request, "dice_page.html", context)

def shop(request):
    dice = Dice.objects.all()
    images = Image.objects.all()
    context = {
        "dice": dice,
        "images": images
    }
    return render(request, "shop.html", context)

def about_page(request):
    return render(request, "about.html")
