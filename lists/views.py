from django.shortcuts import render,HttpResponse,redirect
from lists.models import Item

def home(request):
    if request.method=='POST':
        Item.objects.create(text=request.POST.get('item_text',''))
        return redirect('/')
    return render(request,'html/home.html',{'items':Item.objects.all})
