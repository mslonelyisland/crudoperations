from django.shortcuts import render,redirect
from myapp.forms import OrdersForm  
from myapp.models import Orders

# Create your views here.
def addnew(request):
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else: 
        form = OrdersForm()
    return render(request,'index.html', {'form':form})  
 

def index(request):
    orders = Orders.objects.all()
    return render(request, "show.html", {'orders':orders})

def edit(request, id):
    order = Orders.objects.get(id=id)
    return render(request, 'edit.html', {'order':order}) 

def update(request, id):  
    order = Orders.objects.get(id=id)  
    form = OrdersForm(request.POST, instance = order)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'order': order}) 

def destroy(request, id):  
    order = Orders.objects.get(id=id)  
    order.delete()  
    return redirect("/")  



