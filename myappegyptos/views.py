from django.shortcuts import render,redirect
from .models import Ville
from .forms import VilleForm
from .models import Joueur
from .forms import JoueurForm

# Create your views here.


def list_villes(request):
    villes = Ville.objects.all()
    joueurs = Joueur.objects.all()
    return render(request, 'home.html', {'villes':villes, 'joueurs':joueurs})

def create_ville(request):
    form = VilleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'villes-form.html', {'form': form })

def detail_ville(request,id):
    ville = Ville.objects.get(id = id)

    return render(request, 'ville-detail.html',{'ville':ville})

def update_ville(request,id):
    ville = Ville.objects.get(id = id)
    form = VilleForm(request.POST or None, instance=ville)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'villes-form.html', {'form': form, 'ville' : ville })


def delete_ville(request,id):
    ville = Ville.objects.get(id = id)

    if request.method == "POST":
        ville.delete()
        return redirect('home')

    return render(request, 'ville-delete-confirm.html', {'ville': ville })


def create_joueur(request):
    form = JoueurForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'joueurs-form.html', {'form': form })

def update_joueur(request,id):
    joueur = Joueur.objects.get(id = id)
    form = JoueurForm(request.POST or None, instance=joueur)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'joueurs-form.html', {'form': form, 'joueur' : joueur })


def delete_joueur(request,id):
    joueur = Joueur.objects.get(id = id)

    if request.method == "POST":
        joueur.delete()
        return redirect('home')

    return render(request, 'joueur-delete-confirm.html', {'joueur': joueur })
