from django.shortcuts import render


def homepage(request):
    return render(request, "health_records/index.html")
