from django.shortcuts import render
from . models  import Villa
# Create your views here.


def demo(request):
    obj = Villa.objects.all()
    return render(request, "index.html", {'result': obj})


# def addition(request):
#   x = int(request.GET['num1'])
#  y = int(request.GET['num2'])
#    res = x+y
#    return render(request, "result.html", {'result':res})
