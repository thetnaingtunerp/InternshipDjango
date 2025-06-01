from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def loginview(request):
    return render(request, 'base.html')

def productview(request):
    products = Product.objects.all()
    cates = Category.objects.all()
    context = {'products':products, 'cates':cates}
    return render(request, 'product-list.html', context)

def cartview(request):
    inv_no = request.session.get('invoice_no', None)
    cart = Cart.objects.get(id = inv_no)
    return render(request, 'cart.html', {'cart':cart})

def addtotcart(request):
    pid = request.GET['product_id']
    product_obj = Product.objects.get(id = pid)
    inv_no = request.session.get('invoice_no', None)
    
    if inv_no:
        #have session invoice number
        cart_object = Cart.objects.get(id = inv_no)
        product_exist=cart_object.cartproduct_set.filter(product=product_obj)
        if product_exist.exists():
            product_itm = product_exist.first()
            product_itm.qty += 1
            product_itm.save()
            
        else:
            cp_obj = CartProduct.objects.create(cart= cart_object, product= product_obj, qty= 1,amount= product_obj.price)
        
    else:
        #not session
        cart_object = Cart.objects.create(total_amount=0)
        request.session["invoice_no"] = cart_object.id
        cp_obj = CartProduct.objects.create(cart= cart_object,product= product_obj,qty= 1,amount= product_obj.price)
        
        
        
    
    
    return redirect('/cartview/')


