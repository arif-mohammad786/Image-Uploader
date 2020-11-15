from django.shortcuts import render
from .forms import imageform
from .models import image
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=imageform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    fm=imageform()
    img=image.objects.all()
    return render(request,'myapp/home.html',{'form':fm,'img':img})