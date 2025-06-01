from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

# @login_required(login_url='login')

def loginview(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        pas = request.POST.get('password')
        usr_auth = authenticate(username = usr, password=pas)
        if usr_auth:
            login(request, usr_auth)
            return redirect('/')
        else:
            return redirect('/login/')
        
    else:
        return render(request, 'login.html')





def homepage(request):
    course = Course.objects.all()
    return render(request, 'index.html' , {'course':course})

@login_required(login_url='/login/')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def updatecourse(request, pk):
    course_obj = Course.objects.get(id= pk)
    fm = UpdateCourFm()
    if request.method == 'POST':
        photo = request.FILES['photo_fm']
        name = request.POST.get('name_fm')
        desc = request.POST.get('desc_fm')
        fee = request.POST.get('fee_fm')
        course = Course.objects.filter(id= pk)
        course.update(photo=photo, name=name, fee=fee, description=desc)
        return redirect("{% url 'home'  %}")
    else:
        return render(request, 'updatecourse.html', {'course_obj':course_obj, 'fm':fm})