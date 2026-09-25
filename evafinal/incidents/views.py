from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident
from .forms import IncidentForm

def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incidents/incident_list.html', {'incidents': incidents})

def incident_detail(request, id):
    incident = get_object_or_404(Incident, id=id)
    return render(request, 'incidents/incident_detail.html', {'incident': incident})

def incident_create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/incident_form.html', {'form': form})

def incident_update(request, id):
    incident = get_object_or_404(Incident, id=id)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/incident_form.html', {'form': form})

def incident_delete(request, id):
    incident = get_object_or_404(Incident, id=id)
    incident.delete()
    return redirect('incident_list')