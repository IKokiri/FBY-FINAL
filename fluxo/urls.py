from django.urls import path

from . import views

urlpatterns = [
	path('fluxo/', views.read),
]	