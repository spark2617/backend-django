from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('produtos/', views.produto_list),
    path('produtos/<int:pk>/', views.produto_detail),
    path('vendas-master/', views.vendasMaster_list),
    path('vendas-master/<int:codigo>/', views.vendasMaster_detail),
    path('vendas-detalhe/', views.vendasDetalhe_list),
    path('vendas-detalhe/<int:codigo>/', views.vendasDetalhe_detail),
    path('pessoas/', views.pessoa_list),
    path('pessoas/<int:pk>/', views.pessoa_detail),
]