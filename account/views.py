from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.

def user_login(malumot):
    if malumot.method == "POST":
        form = LoginForm(malumot.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(malumot, username=data['username'], password=data['password'])
            
            if user is not None:
                if user.is_active:
                    login(malumot, user)
                    return HttpResponse("Muvoqiyatli login amalga oshirildi")
                else:
                    return HttpResponse("Sizning profilingiz activ emas")
            else:
                return HttpResponse("User name yoki parolda hato bor")
        else:
            form = LoginForm()
            context = {
                "form": form,
            }
            return render(malumot, "login.html", context)