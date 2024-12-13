from django.urls import path
from . import views

urlpatterns = [
    path('RegisterCloset/', views.register_closet, name='RegisterCloset'),
    path('RegisterClothing/', views.register_clothing, name='RegisterClothing'),
    path('RegisterOutfit/', views.register_outfit, name='RegisterOutfit'),
    path('Fits/', views.fits, name='Fits'),
    path('get_outfits/<int:closet_id>/', views.get_outfits, name='get_outfits'),
    path('check_updates/<int:closet_id>/', views.check_updates, name='check_updates'),
    path('RemoveClothing/', views.remove_clothing, name='RemoveClothing'),
    path('RemoveCloset/', views.remove_closet, name='RemoveCloset'),
    path('RemoveOutfit/', views.remove_outfit, name='RemoveOutfit'),
]