from django.urls import path
from . import views

urlpatterns = [
    path('best_candidates/<int:job_id>', views.candidate_finder)
]