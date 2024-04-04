from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Report_1

# Create your views here.

def check_1(request):
    return render(request, "site_1/index.html")

def check_2(request):
    return render(request, "site_1/services.html")

def check_3(request):
    return render(request, "site_1/Teachers.html")

def check_4(request):
    return render(request, "site_1/Gallery.html")

def check_5(request):
    return render(request, "site_1/About.html")

def check_6(request):
    return render(request, "site_1/Contact.html")

def check_7(request):
    check_report = Report_1.objects.all()
    return render(request, "site_1/graduation.html",  {'call_report': check_report})

def check_8(request):
    return render(request, "site_1/notifications.html")

def check_9(request):
    return render(request, "site_1/education.html")

def check_10(request):
    return render(request, "site_1/registrations.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Drive-school')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'site_1/registrations.html', {'form': form})
