from django.urls import path
from .views import list_villes, create_ville, update_ville, delete_ville, detail_ville, create_joueur, update_joueur,delete_joueur

urlpatterns = [
    path('', list_villes, name='home'),
    path('newVille', create_ville, name='create_ville'),
    path('updateVille/<int:id>/', update_ville, name='update_ville'),
    path('deleteVille/<int:id>/', delete_ville, name='delete_ville'),
    path('detailVille/<int:id>/', detail_ville, name='detail_ville'),
    path('newJoueur', create_joueur, name='create_joueur'),
    path('updateJoueur/<int:id>/', update_joueur, name='update_joueur'),
    path('deleteJoueur/<int:id>/', delete_joueur, name='delete_joueur'),
]
