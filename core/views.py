from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"core/home.html")


# Create your views here.
def contact(request):
    return render(request,"core/contacto.html")

# Create your views here.
def portfolio(request):
    return render(request,"core/portafolio.html")


# Create your views here.
def acercade(request):
    return render(request,"core/acercade.html")

