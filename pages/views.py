from django.shortcuts import render

# Create your views here.


def homepage(request, *args, **kwargs):
    table_num = request.GET.get('table', '0')
    return render(request, "home.html", {'table': table_num})

def bucket_list(request, *args, **kwargs):
    table_num = request.GET.get('table', '0')
    return render(request, "bucket.html", {'table': table_num})
