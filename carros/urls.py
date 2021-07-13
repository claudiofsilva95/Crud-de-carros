from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.IndexList.as_view(), name='index'),
    path('criar-carro/', views.CreateCarro.as_view(), name='criar-carro'),
    path('editar-carro/<int:pk>/', views.UpdateCarro.as_view(), name='editar-carro'),
    path('deletar-carro/<int:pk>/', views.DeleteCarro.as_view(), name='deletar-carro')

]

