from django.urls import path

from . import views

urlpatterns = [
	path('receber/', views.read),
    path('receber/cadastro/', views.cadastro),
    path('receber/create/', views.create),
    path('receber/atualizacao/<int:id>/', views.atualizacao),
    path('receber/update/<int:id>/', views.update),
    path('receber/delete/<int:id>/', views.delete),
]	