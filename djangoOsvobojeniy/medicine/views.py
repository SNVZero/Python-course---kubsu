from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView, UpdateView
import datetime

# Create your views here.
def main(request):
    pacient = Pacient.objects.all()
    diagnosis = Diagnosis.objects.all()
    treatment = Treatment.objects.all()

    card = []

    for el1, el2, el3 in zip(pacient, diagnosis, treatment):
        card.append({'id': el1.id, 'name': el1.NamePac, 'diag': el2.Diagnos, 'treat': el3.MethodOfThreatment})

    return render(request, 'medicine/index.html',
                  {'pacient': pacient, 'treatment': treatment, 'diagnosis': diagnosis, 'card': card})


def create(request):
    if request.method == 'POST':
        pac = PacientForm(request.POST)
        dia = DiagnosisForm(request.POST)
        treat = TreatmentForm(request.POST)

        if pac.is_valid() and dia.is_valid() and treat.is_valid():
            pac.save()
            dia.save()
            treat.save()
            return redirect('home')
        else:
            error = "Неверно заполнены данные"

    pac = PacientForm()
    diag = DiagnosisForm()
    treat = TreatmentForm()
    error = ''

    data = {
        'pac': pac,
        'dia': diag,
        'treat': treat,
        'error': error
    }

    return render(request, 'medicine/edit.html', data)


class PacientInfoDetailView(DetailView):
    template_name = 'medicine/info.html'
    context_object_name = 'card'
    model = Pacient


def update(request, pk):
    try:
        pac = Pacient.objects.get(id=pk)
        dia = Diagnosis.objects.get(id=pk)
        treat = Treatment.objects.get(id=pk)

        if request.method == "POST":
            pac.NamePac = request.POST.get("NameOfPacietn")
            pac.Policy = request.POST.get("NumberOfPart")
            pac.Birth = request.POST.get("YearOfBirth")
            pac.Location = request.POST.get("LocationOfPac")

            dia.Diagnos = request.POST.get("DiseaseName")
            dia.Severity = request.POST.get("Severity")

            treat.MethodOfThreatment = request.POST.get("Treatment")
            treat.DurationOfTreat = request.POST.get("DurationOfTreat")


            pac.save()
            dia.save()
            treat.save()
            return redirect('home')
        else:
            return render(request, "medicine/update.html", {"pac": pac, "dia": dia, "treat": treat})
    except pac.DoesNotExist and dia.DoesNotExist and treat.DoesNotExist:
        return redirect("home")

def delete(request,pk):
    pac = Pacient.objects.get(id=pk)
    dia = Diagnosis.objects.get(id=pk)
    treat = Treatment.objects.get(id=pk)
    if request.method == 'POST':
        pac.delete()
        dia.delete()
        treat.delete()
        return redirect('home')
    else:
        return render(request, "medicine/delete.html", {"pac": pac})
