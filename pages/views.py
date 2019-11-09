from django.shortcuts import render

# Create your views here.
def homepage(request, *args, **kwargs):
   # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})
