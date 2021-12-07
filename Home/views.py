from django.shortcuts import render
from django.contrib import messages
from Home.models import signup
from Home.models import news


# Create your views here.
def home(request):
   
    return render(request, 'home.html')  

def Registration(request):
    if request.method == "POST":
        Name  = request.POST.get('Name')
        Phone  = request.POST.get('Phone')   
        City  = request.POST.get('City')
        State  = request.POST.get('State')
        District  = request.POST.get('District')
        Registration = signup(Name=Name, Phone=Phone, City=City, District=District, State=State)
        Registration.save()
        messages.success(request, ' Submition Successfull')
    return render(request, 'registration.html')    
def about(request):
    return render(request, 'about.html')    
def players(request):
    data = signup.objects.all()
    go = {'data':data }

    return render(request, 'playerlist.html', go )
def player(request):

    return render(request, 'player.html' )
def News(request):
    data2 = news.objects.all()
    go2 = {'data2':data2 }

    return render(request, 'news.html',go2 )
