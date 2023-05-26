from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def homePage(request):
    users = crudUser.objects.all().order_by('firstname')
    return render(request, "main/home.html", {'users':users})


def createUser(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:homePage")
    else:
        form = userForm()

    return render(request, "main/createUser.html", {'form':form})


def modifyUser(request, pk):
    user = crudUser.objects.get(id=pk)
    form = userForm(instance=user)

    if request.method == "POST":
        form = userForm(request.POST, instance=user)
        if form.is_valid():
            user.firstname = form.cleaned_data.get('firstname')
            user.lastname = form.cleaned_data.get('lastname')
            user.email = form.cleaned_data.get('email')
            user.password = form.cleaned_data.get('password')
            user.save()
            return redirect("main:homePage")

    return render(request, "main/modifyUser.html", {'form':form})


def deleteUser(request, pk):
    user = crudUser.objects.get(id=pk)
    form = deleteForm()

    if request.method == "POST":
        form = deleteForm(request.POST)
        if form.is_valid():
            yes = form.cleaned_data.get("yes")
            no = form.cleaned_data.get("no")
            if yes:
                user.delete()
            return redirect("main:homePage")

    context = {
        'form': form, 'user': user,
    }
    return render(request, "main/deleteUser.html", context)
