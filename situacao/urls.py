from django.urls import path

from . import views

urlpatterns = [
	path('situacao/', views.read),
    path('situacao/cadastro/', views.cadastro),
    path('situacao/create/', views.create),
    path('situacao/atualizacao/<int:id>/', views.atualizacao),
    path('situacao/update/<int:id>/', views.update),
    path('situacao/delete/<int:id>/', views.delete),
]	