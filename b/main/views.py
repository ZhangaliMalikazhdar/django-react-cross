from django.shortcuts import render

def react_app(request):
    return render(request, 'build/index.html')
