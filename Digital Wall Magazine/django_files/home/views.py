from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Homepage")

def blogs(request):
    return HttpResponse("This is Blogs")

def art_gallery(request):
    return HttpResponse("This is Art Gallery")

def notices(request):
    return HttpResponse("This is Notices")

def about_us(request):
    return HttpResponse("This is About Us")