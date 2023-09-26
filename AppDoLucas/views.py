from django.shortcuts import render, redirect, get_object_or_404
from .models import Idolo, Experiencia, Titulo
from .forms import IdoloForm, UpdateIdoloForm, DeleteIdoloForm, ExperienciaForm, ExperienciaUpdateForm, ExperienciaDeleteForm

def home(request):
    idolos = Idolo.objects.all()
    exp = Experiencia.objects.all()
    titulos = Titulo.objects.all()
    
    if request.method == 'POST':
        idolo_form = IdoloForm(request.POST, request.FILES)
        if idolo_form.is_valid():
            idolo_form.save()  
            return redirect('home')  
    else:
        idolo_form = IdoloForm()

    return render(request, "home.html", context={"idolos": idolos, "exp": exp, "titulos": titulos, "idolo_form": idolo_form})

def create_idolo(request):
    if request.method == 'POST':
        idolo_form = IdoloForm(request.POST, request.FILES)
        if idolo_form.is_valid():
            idolo_form.save()
            return redirect('home')
    else:
        idolo_form = IdoloForm()

    return render(request, 'forms.html', context={'action': 'Adicionar Ídolo', 'idolo_form': idolo_form})

def update_idolo(request, id):
    idolo = get_object_or_404(Idolo, id=id)

    if request.method == 'POST':
        idolo_form = UpdateIdoloForm(request.POST, instance=idolo)
        if idolo_form.is_valid():
            idolo_form.save()
            return redirect('home')

    else:
        idolo_form = UpdateIdoloForm(instance=idolo)

    return render(request, 'forms.html', context={'action': 'Atualizar', 'form': idolo_form})

def delete_idolo(request, id):
    idolo = get_object_or_404(Idolo, id=id)

    if request.method == 'POST':
        delete_form = DeleteIdoloForm(request.POST, instance=idolo)
        if 'confirm' in request.POST:
            idolo.delete()
            return redirect('home')

    else:
        delete_form = DeleteIdoloForm()

    return render(request, 'tem_ctz.html', context={'idolo': idolo, 'delete_form': delete_form})

def create_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExperienciaForm()

    context = {'form': form,}

    
    return render(request, 'create_experiencia.html', context)

def update_experiencia(request, id):
    experiencia = Experiencia.objects.get(id=id)
    if request.method == 'POST':
        experiencia_form = ExperienciaUpdateForm(request.POST, instance=experiencia)
        if experiencia_form.is_valid():
            experiencia_form.save()
            return redirect('home')
    else:
        experiencia_form = ExperienciaUpdateForm(instance=experiencia)
    
    return render(request, 'update_experiencia.html', context={'form': experiencia_form, 'experiencia': experiencia})

def delete_experiencia(request, id):
    experiencia = Experiencia.objects.get(id=id)
    if request.method == 'POST':
        experiencia_form = ExperienciaDeleteForm(request.POST, instance=experiencia)
        if experiencia_form.is_valid() and "confirm" in request.POST:
            experiencia.delete()
            return redirect('home')
    else:
        experiencia_form = ExperienciaDeleteForm(instance=experiencia)
    
    return render(request, 'tem_ctz_exp.html', context={'form': experiencia_form, 'experiencia': experiencia})