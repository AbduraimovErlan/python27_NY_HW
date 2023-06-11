from . import views
from django.urls import path




urlpatterns =[
    path('authorization/', views.authorization_view),
    path('registration/', views.registration_view),
    path('confirm/', views.confirm_user_view),
]