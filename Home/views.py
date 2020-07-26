from django.shortcuts import render
from django.contrib import messages
from Home.models import signup

# Create your views here.
def home(request):
   
    return render(request, 'home.html')  

def Registration(request):
    if request.method == "POST":
        Name  = request.POST.get('Name')
        Phone  = request.POST.get('Phone')   
        PubgID  = request.POST.get('PubgID')
        City  = request.POST.get('City')
        Pic  = request.POST.get('Pic')
        State  = request.POST.get('State')
        District  = request.POST.get('District')
        Registration = signup(Name=Name, Phone=Phone, PubgID=PubgID, City=City, District=District, State=State,Pic=Pic)
        Registration.save()
        messages.success(request, ' Submition Successfull')
    return render(request, 'registration.html')    
def about(request):
    return render(request, 'about.html')    
def playerlist(request):
    data = signup.objects.all()
    go = {'data':data }

    return render(request, 'playerlist.html', go )
def players(request):

    return render(request, 'player.html' )