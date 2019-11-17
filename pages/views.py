from django.shortcuts import render
#from Burgers.models import Burger

# Create your views here.
def homepage(request, *args, **kwargs):

    way = 'media/' + str(Burger.objects.get(id=5).img)
    return render(request, "home.html", {'image': way})

