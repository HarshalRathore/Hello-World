from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from level_plan.models import Plans

def dashboard(request):
    return render(request, 'dashboard.html')

def plans(request):
    return render(request, 'plans.html')