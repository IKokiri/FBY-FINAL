from django.urls import path

from . import views

urlpatterns = [
	path('transacao/', views.read),
    path('transacao/cadastro/', views.cadastro),
    path('transacao/create/', views.create),
    path('transacao/atualizacao/<int:id>/', views.atualizacao),
    path('transacao/update/<int:id>/', views.update),
    path('transacao/delete/<int:id>/', views.delete),
]	