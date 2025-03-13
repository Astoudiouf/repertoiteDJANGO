from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm





def Login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect("/contact/")  
            
            else:
                form.add_error(None, "Nom d'utilisateur ou mot de passe incorrect")
    else:
        form = LoginForm()

    return render(request, "utilisateur/login.html", {"form": form}) 



def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST) 
        if form.is_valid():
            user = form.save()  
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=raw_password)
            return redirect("/login/")  
    else:
        form = SignUpForm()

    return render(request, "utilisateur/register.html", {"form": form})


