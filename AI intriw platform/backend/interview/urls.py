from django.urls import path
from .views import start_interview, submit_answer,signup,login_user

urlpatterns = [
    path('start/', start_interview),
    path('submit/', submit_answer),
    # path('stop/', stop_interview),
    path("signup/", signup),
    path("login/", login_user),
]