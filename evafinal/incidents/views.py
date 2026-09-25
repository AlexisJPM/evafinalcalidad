from django.shortcuts import render, redirect
from .forms import IncidentForm
from .services.incident_service import IncidentService

def incident_list(request):
    incidents = IncidentService.get_all_incidents()
    return render(request, 'incidents/incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = IncidentService.get_incident_by_id(pk)
    return render(request, 'incidents/incident_detail.html', {'incident': incident})

def incident_create(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if IncidentService.save_incident(form):
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/incident_form.html', {'form': form, 'action': 'Crear'})

def incident_update(request, pk):
    incident = IncidentService.get_incident_by_id(pk)
    if request.method == 'POST':
        form = IncidentForm(request.POST, instance=incident)
        if IncidentService.save_incident(form):
            return redirect('incident_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/incident_form.html', {'form': form, 'action': 'Editar'})

def incident_delete(request, pk):
    incident = IncidentService.get_incident_by_id(pk)
    if request.method == 'POST':
        IncidentService.delete_incident(incident)
        return redirect('incident_list')
    return render(request, 'incidents/incident_delete.html', {'incident': incident})