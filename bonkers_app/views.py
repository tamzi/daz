from django.shortcuts import render

# Create your views here.
def bonkers(request):
    return render(request, 'bonkers_app.html', {})
