from django.urls import path
from . import views

# caminho de cada funçao
urlpatterns = [
  path('', views.home, name = 'home'),
  path('adicionarEvento', views.addEvento, name = 'addEvento'),
  path('MeusEvento', views.meusEventos, name = 'meusEventos'),
  path('<id>/', views.detalharEvento, name = 'detalharEvento'),
  path('<id>/editar', views.editarEvento, name = 'editarEvento'),
  path('<id>/deletar', views.deletarEvento, name = 'deletarEvento'),
]