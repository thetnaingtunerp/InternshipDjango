from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    cat = Category.objects.all()
    itm = Items.objects.all()
    context = {'cat':cat, 'itm':itm}
    return render(request, 'index.html', context)


def createcate(request):
    cat = request.GET['itemname']
    cat = request.GET['iprice']
    cat = request.FILES['iphoto']
    Category.objects.create(category_name=cat)
    return redirect('/admin/')


# def insertitem(request):
#     cid = 1
#     cat_obj = Category.objects.get(id=cid)
#     name = Apple
#     phto = 
#     price =
#     Item.objects.create(category = cat_obj)


def AddtoCart(request):
    qty = request.POST['iqty']
    itmid = request.POST['itmid']
    itm_obj = Items.objects.get(id = itmid)
    total= itm_obj.price * qty
    CartItem.objects.create(
        items= itm_obj,
        qty= qty,
        price= itm_obj.price,
        total_amount= total        
        )
    return redirect('/')