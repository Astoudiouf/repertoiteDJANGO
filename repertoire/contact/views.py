
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import contact




def home(request):
  return render(request, "index.html")

def about(request):
  return render(request, "about.html")


@login_required(login_url="/login/")
def liste_des_contacts(request):
  user =request.user
  contacts = contact.objects.filter(auteur=user, archive=False)
  return render(request, "contact/liste_des_contacts.html", {'contacts': contacts})


@login_required(login_url="/login/")
def contact_details(request,id):
  contacts=get_object_or_404(contact,id=id)
  return render(request,"contact/contact_details.html",{"contacts":contacts})


@login_required(login_url="/login/")
def new_contact(request):
  if request.method == "POST":
    auteur = request.user
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    telephone=request.POST['telephone']
    email=request.POST['email']
    contacts=contact.objects.create(
      auteur=auteur,
      nom=nom,
      prenom=prenom,
      telephone=telephone,
      email=email,
    )
    contacts.save()
    return redirect("/contact/")
  return render(request ,"contact/new_contact.html")


@login_required(login_url="/login/")
def edit_contact(request, id):
  contacts=get_object_or_404(contact, id=id)
  if request.method == "POST":
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    telephone=request.POST['telephone']
    email=request.POST['email']
    contact_to_update=contact.objects.filter(pk=contacts.id)
    contact_to_update.update(
      nom=nom,
      prenom=prenom,
      telephone=telephone,
      email=email,)
    return redirect("/contact/")
  return render(request, "contact/edit_contact.html", {"contacts":contacts})


@login_required(login_url="/login/")
def delete_contact(request, id):
  contacts =get_object_or_404 (contact, id=id)
  if request.method=="POST":
    contact_to_archive=contact.objects.filter(pk=contacts.id)
    contact_to_archive.update(
      archive=True
    )
    # contacts.delete()
    return redirect("/contact/")
  return render(request,"contact/delete_contact.html",{"contacts":contacts})
  