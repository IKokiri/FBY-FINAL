from django.urls import path

from . import views

urlpatterns = [
	path('pagar/', views.read),
    path('pagar/cadastro/', views.cadastro),
    path('pagar/create/', views.create),
    path('pagar/atualizacao/<int:id>/', views.atualizacao),
    path('pagar/update/<int:id>/', views.update),
    path('pagar/delete/<int:id>/', views.delete),
]	