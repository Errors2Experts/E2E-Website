from .models import SiteOffer,Career

def latest_offer(request):
    # Gets the latest active offer
    offer = SiteOffer.objects.filter(is_active=True).order_by('-created_at').first()
    job_vacancies = Career.objects.all()
    return {'active_offer': offer, 'careers': job_vacancies}