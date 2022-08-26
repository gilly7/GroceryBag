from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item

@login_required
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        status = request.POST.get("status")
        date = request.POST.get("date")
        if name and quantity and status and date:
            new_item = Item(name=name, quantity=quantity,
                            status=status, date=date, user=request.user)
            new_item.save()
            messages.success(request, 'Item added successfully!')
            return redirect('index')
        messages.error(request, "One or more field(s) is missing!")
        return redirect('add-item')
    return render(request, "add.html")