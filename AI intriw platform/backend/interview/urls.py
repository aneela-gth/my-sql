from django.urls import path
from .views import start_interview, submit_answer

urlpatterns = [
    path('start/', start_interview),
    path('submit/', submit_answer),
    # path('stop/', stop_interview),
]