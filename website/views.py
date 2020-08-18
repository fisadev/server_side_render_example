from django.shortcuts import render

from website.models import Visit


def home(request):
    new_visit = Visit()
    new_visit.save()

    total_visits = Visit.objects.all().count()

    return render(request, "home.html", {'total_visits': total_visits})
