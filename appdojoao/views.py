from django.shortcuts import render, redirect
from .models import Mapas, Armas, TabelaMapas
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  mapas = Mapas.objects.all()
  armas = Armas.objects.all()
  locais = TabelaMapas.objects.all()
  return render(request, 'home.html', context={"mapas":mapas, "armas":armas, "locais":locais})

def style(request):
  return render(request, 'style.css')

def create_maps(request):
  if request.method == "POST":
    Mapas.objects.create(
      name = request.POST["name"],
      local = request.POST["local"],
      modos = request.POST["modos"]
    )
    return redirect("home")
  return render(request, "forms_mapas.html", context={"action" : "Adicionar"})

def update_maps(request, id):
  mapa = Mapas.objects.get(id = id)
  
  if request.method == "POST":
    mapa.name = request.POST["name"],
    mapa.local = request.POST["local"],
    mapa.modos = request.POST["modos"]
    mapa.save()
    
    return redirect("home")
  return render(request, "forms_mapas.html", context={"action" : "Atualizar", "mapa" : mapa})

def delete_maps(request, id):
  mapa = Mapas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      mapa.delete()

    return redirect("home")
  return render(request, "temCtz_mapas.html", context={"mapa": mapa})

def create_guns(request):
  if request.method == "POST":
    Armas.objects.create(
      nome = request.POST["nome"],
      origem = request.POST["origem"],
      calibre = request.POST["calibre"]
    )
    return redirect("home")
  return render(request, "forms_armas.html", context={"action" : "Adicionar"})

def update_guns(request, id):
  arma = Armas.objects.get(id = id)
  
  if request.method == "POST":
    arma.nome = request.POST["nome"],
    arma.origem = request.POST["origem"],
    arma.calibre = request.POST["calibre"]
    arma.save()
    
    return redirect("home")
  return render(request, "forms_armas.html", context={"action" : "Atualizar", "arma" : arma})

def delete_guns(request, id):
  arma = Armas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      arma.delete()

    return redirect("home")
  return render(request, "temCtz_armas.html", context={"arma": arma})

def create_mapsTab(request):
  if request.method == "POST":
    TabelaMapas.objects.create(
      nome = request.POST["nome"],
      local = request.POST["local"],
    )
    return redirect("home")
  return render(request, "forms_mapasTab.html", context={"action" : "Adicionar"})

def update_mapsTab(request, id):
  local = TabelaMapas.objects.get(id = id)
  
  if request.method == "POST":
    local.nome = request.POST["nome"],
    local.local = request.POST["local"],
    local.save()
    
    return redirect("home")
  return render(request, "forms_mapasTab.html", context={"action" : "Atualizar", "local" : local})

@login_required
def home(request):
  arma = Armas.objects.all()
  mapa = Mapas.objects.all()
  local = TabelaMapas.objects.all()
  
  return render(request, "home.html", context={ 
    "arma": arma,
    "mapa": mapa,
    "local": local
  })

@login_required
def create_mapa(request):
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    Mapas.objects.create(
      name = request.POST["name"],
      local = request.POST["local"],
      modos = request.POST["modos"],
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

@login_required
def update_mapa(request, id):
  mapa = Mapas.objects.get(id = id)
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    mapa.name = request.POST["name"]
    mapa.local = request.POST["local"]
    mapa.modos = request.POST["modos"]
    mapa.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","mapa": mapa})

@login_required
def delete_mapa(request, id):
  mapa = Mapas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      mapa.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"mapa": mapa})

@login_required
def create_arma(request):
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    Armas.objects.create(
      nome = request.POST["nome"],
      origem = request.POST["origem"],
      calibre = request.POST["calibre"],
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

@login_required
def update_arma(request, id):
  arma = Armas.objects.get(id = id)
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    arma.nome = request.POST["name"]
    arma.origem = request.POST["origem"]
    arma.calibre = request.POST["calibre"]
    arma.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","arma": arma})

@login_required
def delete_arma(request, id):
  arma = Armas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      arma.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"arma": arma})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")