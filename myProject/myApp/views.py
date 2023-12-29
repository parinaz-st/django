from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {}
    return render(request, "myApp/hello.html", context)
