from django.urls import path

from . import views

urlpatterns = [
	path('classificacao/', views.read),
    path('classificacao/cadastro/', views.cadastro),
    path('classificacao/create/', views.create),
    path('classificacao/atualizacao/<int:id>/', views.atualizacao),
    path('classificacao/update/<int:id>/', views.update),
    path('classificacao/delete/<int:id>/', views.delete),
]	