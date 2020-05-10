from django.shortcuts import render

# Create your views here.

humans = [
    {'name': 'derek', 'age': 18, 'sex': 'boy'},
    {'name': 'jennie', 'age': 16, 'sex': 'girl'},
    {'name': 'barry', 'age': 17, 'sex': 'girl'},
]

def index(request):
    return render(request, 'index.html', {'humans': humans})

