from django.shortcuts import render,HttpResponse, redirect
from .models import *
# Create your views here.
def home(request):
    sample_data = SampleTbl.objects.all()
    return render(request, 'index.html', {'data':sample_data})

def about(request):
    return render(request, 'about.html')

def savedata(request):
    name_data = request.GET['name_fm']
    age_data = request.GET['age_fm']
    
    SampleTbl.objects.create(name=name_data, age= age_data)
    sample_data = SampleTbl.objects.all()
    
    return render(request, 'index.html', {'data':sample_data})

def deletedata(request, pk):
    obj = SampleTbl.objects.filter(id = pk)
    obj.delete()
    # return render(request, 'index.html')
    return redirect('/homepage/')

def deatailpage(request, pk):
    data = SampleTbl.objects.get(id= pk)
    if request.method == 'POST':
        get_qty = request.POST['qty']
        subtotal = data.age * get_qty
        balance = data.qty - get_qty
        data.update(qty= balance)
        
    return render(request, 'detail.html', {'data':data})


def addtocart(request, pk):
    pro_obj = SampleTbl.objects.get(id=pk)
    # qty = request.POST['qty']
    qty = 2
    sub = pro_obj.age * qty
    
    SampleReport.objects.create(name=pro_obj.name , color=pro_obj.color, size =pro_obj.size , saleprice = pro_obj, qty =qty , subtotal=sub)
    
    redirect('/')


