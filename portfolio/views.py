from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def projects(request):
    projects_list = [
        {'title': 'E-Commerce Website', 'desc': 'Built with Django & React.'},
        {'title': 'Weather App', 'desc': 'Uses OpenWeather API.'},
        {'title': 'Portfolio Site', 'desc': 'Dynamic portfolio built with Django.'},
    ]
    return render(request, 'projects.html', {'projects': projects_list})

def contact(request):
    return render(request, 'contact.html')
