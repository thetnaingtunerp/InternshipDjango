from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *

from django.views.generic import TemplateView

# Create your views here.
def postdata(request):
    post_data = Post.objects.all()
    
    context = {'data':post_data}
    return render(request, 'posts.html', context)


def myfriends(request):
    friends = Myfriend.objects.all()
    mylist = [1,2,3,4,]
    context ={'friends':friends, 'my': mylist}
    return render(request, 'myfriend.html', context)


def postdetail(request, pk):
    data = Post.objects.filter(id = pk)
    getdata = Post.objects.get(id = pk) #single query
   
    context ={"data":data, 'getdata':getdata}
    return render(request, 'detail.html', context)

#from .forms import *
def createpost(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('post_body')
        photo = request.FILES.get('photo')
        print(title)
        print(body)
        print(photo)
        query = Post.objects.create(title=title,post_body=body,photo=photo)
        print('Success.....')
        return redirect("/posts/")
    return render(request, 'createpost.html')

def createfrom(request):
    fm = PostModelForm()
    if request.method == "POST":
        fm = PostModelForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('/posts/')
        else:
            return HttpResponse('Error')
    return render(request, 'createpost.html', {'fm':fm})


def bloglist(request):
    getdata = Blog.objects.all()
    return render(request, 'bloglist.html', {'getdata':getdata})

def blogdetail(request, pk):
    data = Blog.objects.get(id=pk)
    return render(request, 'detail.html', {'data':data})


def blogupdate(request, pk):
    data = Blog.objects.get(id=pk)
    name = request.get('')
    
    fm = BlogModelForm1(request.POST, request.FILES, instance=data)
    if fm.is_valid():
            fm.save()
    return redirect('/bloglist/')




def deleteblog(request, pk):
    data = Blog.objects.get(id=pk)
    data.delete()
    return redirect('/bloglist/')

def createblog(request):
    blog_form = BlogModelForm()
    return render(request, 'createblog.html', {'blog_form':blog_form})

def saveblog(request):
    if request.method == "POST":
        blog_form = BlogModelForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            print('Blog Save Success ....')
            return redirect('/bloglist/')
        else:
            return HttpResponse('Error Having')
            



# Function Base View (FBV)
# CBV - Class Base View 



        