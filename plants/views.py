from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Plant
from django.contrib.auth import login, authenticate , logout
# Create your views here. 
def index(request): 
    tallest_plants = Plant.objects.order_by('-height')[:15] 
    context = {'tallest_plants': tallest_plants} 
    return render(request, 'plants/index.html', context)
    
# Create your views here.
def show(request, plant_id): 
    try: 
        plant = Plant.objects.get(pk=plant_id) 
    except Plant.DoesNotExist: 
        raise Http404("Plant does not exist") 
    return render(request, 'plants/show.html', {'plant': plant})
    
def add_plant(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method == "POST":
            print("request submitted")
            name = request.POST.get("name")
            print(name)
            country = request.POST.get("country")
            climate = request.POST.get("climate")
            soil = request.POST.get("soil")
            family = request.POST.get("family")
            height = request.POST.get("height")
            user_id = request.POST.get("user_id")
        return render(request, 'plants/add_plant.html' , {'current_user': current_user})
    else:
        return redirect("index")