from django.urls import path
import level_plan.views as views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('plans/', views.plans, name='plans'),
]
