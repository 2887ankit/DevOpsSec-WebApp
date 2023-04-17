from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from .models import Plant
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages
# Create your views here. 
def index(request): 
    tallest_plants = Plant.objects.order_by('-height')[:15] 
    context = {'tallest_plants': tallest_plants} 
    return render(request, 'plants/index.html', context)
    
# Create your views here.
def show(request, plant_id): 
    try: 
        plant = Plant.objects.get(pk=plant_id)
        print(plant); 
    except Plant.DoesNotExist: 
        raise Http404("Plant does not exist") 
    return render(request, 'plants/show.html', {'plant': plant})
    
def add_plant(request):
    if request.user.is_authenticated:
        current_user=request.user
        if request.method == "POST":
            name = request.POST.get("name")
            country = request.POST.get("country")
            climate = request.POST.get("climate")
            soil = request.POST.get("soil")
            family = request.POST.get("family")
            height = request.POST.get("height")
            user_id = request.POST.get("user_id")
            print(name,country,climate,soil,family,height,user_id) 
            query=Plant(name=name,country=country,climate=climate,soil=soil,family=family,height=height,user_id=user_id) #We called here our class function "Plant" from model.py.
            query.save() #This is to save the particular Data that we are entering to be stored in DB
            messages.info(request,"New Plant data Inserted Successfully")
            return redirect("/plants")
        return render(request, 'plants/add_plant.html' , {'current_user': current_user})
    else:
        return redirect("index")
        
def update(request,id):
    try:
        if request.method=="POST":
            name=request.POST['name']
            country=request.POST['country']
            climate=request.POST['climate']
            soil=request.POST['soil']
            family=request.POST['family']
            height=request.POST['height']
            
            edit = Plant.objects.get(id=id)
            edit.name = name
            edit.country = country
            edit.climate = climate
            edit.soil = soil
            edit.family = family
            edit.height = height
            edit.save()
            messages.warning(request,"Plant Data Updated Successfully")
            return redirect("/plants")
            
        plant = Plant.objects.get(pk=id)
        
    except Plant.DoesNotExist: 
        raise Http404("Plant does not exist") 
    return render(request, 'plants/update_plant.html' ,{'plant': plant})
    
def delete(request,id):
    context ={}
    plant = Plant.objects.get(id=id)
 
 
    if request.method =="POST":
        plant.delete()
        messages.error(request,"Plant Data Deleted Successfully")
        # after deleting redirect to Plant
        return redirect("/plants")
 
    return render(request, "plants/delete_plant.html", context)