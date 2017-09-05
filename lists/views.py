from django.shortcuts import render,HttpResponse,redirect
from lists.models import Item,List


def homepage(request):
    return render(request, 'html/home.html')


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text'), list=list_)
    return redirect('/lists/%d/' % (list_.id,))


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request,'html/list.html', {'list': list_})


def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
