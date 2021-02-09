from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import item

# get all the items
def HomePage(request):
    all_items = item.objects.all()
    return render(request, "home.html", {"all_items": all_items})


# add an item
def addItem(request):
    content = request.POST["content"]
    new_item = item(content=content, name="chocolate", price=111)
    new_item.save()
    return HttpResponseRedirect("/home/")


# delete an item
def deleteItem(request, item_id):
    Deleteitem = item.objects.get(id=item_id)
    Deleteitem.delete()
    return HttpResponseRedirect("/home/")


# update an item
def updateItem(request, item_id):
    updateItem = item.objects.get(id=item_id)
    return render(request, "update.html", {"updateItem": updateItem})


def updateItemPage(request):
    updated_Item = item(
        id=request.POST["item_id"],
        content=request.POST["content"],
        name=request.POST["name"],
        price=request.POST["price"],
    )
    updated_Item.save()
    return HttpResponseRedirect("/home/")


def itemDetailsView(request, item_id):
    requireditem = item.objects.get(id=item_id)
    return render(request, "itemDetailsPage.html", {"item": requireditem})