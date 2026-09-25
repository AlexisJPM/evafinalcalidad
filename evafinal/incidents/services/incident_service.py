from ..models import Incident

class IncidentService:

    @staticmethod
    def get_all_incidents():
        return Incident.objects.all()

    @staticmethod
    def get_incident_by_id(incident_id):
        return Incident.objects.filter(id=incident_id).first()

    @staticmethod
    def save_incident(form):
        if form.is_valid():
            return form.save()
        return None

    @staticmethod
    def delete_incident(incident):
        if incident:
            incident.delete()
            return True
        return False