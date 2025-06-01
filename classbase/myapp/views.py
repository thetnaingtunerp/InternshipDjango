from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import TemplateView,View, ListView, DeleteView,DetailView
from .models import *
from django import forms
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
class First(TemplateView):
    template_name = 'tableexample.html'
    
class Second(View):
    def get(self, request):
        print('This is GET Method')
        return render(request, 'index.html')
    
    def post(self, request):
        print('POST Method is working......,')
        return render(request, 'index.html')
    
    def put(self, request):
        pass

#Model Form
class IncomeExpenseForm(forms.ModelForm):
    class Meta:
        model = IncomeExpense
        fields = ['task_name','amount', 'category']


def trackerlist(request):
    mylist = IncomeExpense.objects.all()
    fm = IncomeExpenseForm()
    paginator = Paginator(mylist, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        saveform = IncomeExpenseForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/')
        else:
            return HttpResponse('Error')
    return render(request, 'index.html', {'mylist':mylist, 'fm':fm, "page_obj": page_obj})






class ExpenseList(View):
    def get(self, request):
        mylist = IncomeExpense.objects.all()
        fm = IncomeExpenseForm()
        return render(request, 'index.html', {'mylist':mylist, 'fm':fm})
    
    def post(self, request):
        saveform = IncomeExpenseForm(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/')
        

def updatedata(request, pk):
    ie = IncomeExpense.objects.get(id=pk)
    fm = IncomeExpenseForm(instance=ie)
    if request.method == "POST":
        fm = IncomeExpenseForm(request.POST,instance=ie)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    context = {'ie':ie, 'fm':fm}
    return render(request, 'update.html', context)

class UpdateTracker(View):
    def get(self, request, pk):
        ie = IncomeExpense.objects.get(id=pk)
        fm = IncomeExpenseForm(instance=ie)
        context = {'ie':ie, 'fm':fm}
        return render(request, 'update.html', context)
    
    def post(self, request, pk):
        ie = IncomeExpense.objects.get(id=pk)
        fm = IncomeExpenseForm(request.POST,instance=ie)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        

        
class CateList(ListView):
    model = Category
    template_name = 'index.html'   
    
class CateDetail(DetailView):
    model = Category 
    context_object_name = "cat"
    template_name = 'category_detail.html'
    
#  from django.http import JsonResponse    
def create_expense(request):
    task = request.GET['expense']
    amt = request.GET['amount']
    cate= request.GET['cat']
    category_obj = Category.objects.get(id= int(cate))
    IncomeExpense.objects.create(
        task_name = task,
        amount = amt,
        category = category_obj
    )
    print('success')
    return JsonResponse({'status':'success'})
  
def delete_exp(request):
    pid = request.GET['pd']
    pd = IncomeExpense.objects.get(id= int(pid))
    pd.delete()
    return JsonResponse({'status':'success'})


def categorylist(request):
    data = list(IncomeExpense.objects.all().values())
    
    return JsonResponse({'iedata':data})


def regiser_view(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password1']
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        usr = User.objects.filter(username = username)
        if usr.exists():
            return redirect('/regiser_view/')
        else:
            user_obj=User.objects.create_user(username = username, first_name= firstname, last_name= lastname)
            user_obj.set_password(password)
            user_obj.is_staff = True
            user_obj.save()
            return redirect('/')
    else:
        return render(request, 'register.html')
    
class UserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect('/regiser_view/')
        return super().dispatch(request, *args, **kwargs)


class SuperUser(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            pass
        else:
            return redirect('/regiser_view/')
        return super().dispatch(request, *args, **kwargs)
    
class HomeView(UserRequiredMixin,View):
    def get(self, request):
        return render(request, 'index.html')

from django.contrib.auth import authenticate,login,logout    

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
    
  
