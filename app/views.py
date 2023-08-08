from django.shortcuts import render

# Create your views here.
def collapse(request):
    return render(request,'collapse.html')
def dropdowns(request):
    return render(request,'dropdowns.html')
def forms(request):
    return render(request,'forms.html')
def Input_group(request):
    return render(request,'Input_group.html')
def jumbotron(request):
    return render(request,'jumbotron.html')
def list_group(request):
    return render(request,'list_group.html')
def media_object(request):
    return render(request,'media_object.html')