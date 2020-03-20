from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import EditProfileForm
from plan.models import Booker, Flights, PlannedFlights

@login_required(login_url='/')
def checkout(request):
    return render(request, "checkout.html", {})


@login_required(login_url='/')
def details(request, pk):

    pl_b = PlannedFlights.objects.filter(id=pk)


    context = {
        'detail' : pl_b
    }
    return render(request, "details.html", context)

@login_required(login_url='/')
def schedules(request):

    pl_b = PlannedFlights.objects.filter(user_id=request.user.id)

    context = {
        'sched' : pl_b
    }
    return render(request, "schedules.html", context)

@staff_member_required(login_url='/')
def del_flights(request, pk):
    query = Flights.objects.get(id=pk)
    query.delete()
    return redirect('flights')

@login_required(login_url='/')
def flights(request):


        
    context = {
        'flights' : Flights.objects.all()
    }
    return render(request, "flights.html", context)


@login_required(login_url='/')
def home(request):
    return render(request, "home.html", {})


@login_required(login_url='/')
def profile(request):
    return render(request, "profile.html", {})


@login_required(login_url='/')
def settings(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updates has been successful.')
            return redirect('settings')

    else:
        form = EditProfileForm(request.POST, instance=request.user)

    context = {'form': form}
    return render(request, 'settings.html', context)
