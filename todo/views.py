# from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
# from .models import Item
# from .forms import ItemForm

# # Create your views here.
# def get_todo_list(request):
#     results = Item.objects.all()
#     return render(request, 'todo_list.html', {'items': results}) # render() is similiar to HttpResponse()
    
# def create_an_item(request):
#     if request.method == "POST":
#         form = ItemForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(get_todo_list)
#     else: # If the request is not a post request
#         form = ItemForm() # Just return an empty form
        
#     return render(request, 'item_form.html', {'form': form})
    
# def edit_an_item(request, id): # We pass the id in here so it can be passed into the url
#     # get_object_or_404 works by throwing a 404 error if it cannot find a particular instance
#     item = get_object_or_404(Item, pk = id) # Create a new instance of an item, the specific item you want is the one with a primary key equal to the id
    
#     if request.method == "POST":
#         form = ItemForm(request.POST, instance=item)
#         if form.is_valid(): # This does the server side form validation
#             form.save()
#             return redirect(get_todo_list)
#         else:
#             form = ItemForm(instance = item)
        
#     form = ItemForm(instance = item) # Create a form and pass in item as the instance that we want to construct the object from
#     return render(request, 'item_form.html', {'form': form})
    
# def done_status(request, id):
#     item = get_object_or_404(Item, pk = id)
#     item.done = not item.done # If the item is done it will be set to not done, if the item is not done it will bet set to done
#     item.save()
#     return redirect(get_todo_list)

"""Code Institute's github source code is below. Using because for some reason you was only getting 97% test coverage for views"""

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {
        'items': results
    })


def create_an_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    return render(request, "item_form.html", {'form': form})


def edit_an_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, "item_form.html", {'form': form})


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)