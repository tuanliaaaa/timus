from django.urls import path
from . import views
urlpatterns = [
    path('home',views.index,name='home'),
    path('watches',views.watches,name='watch'),
    path('watches/showAll',views.showAll,name='watches'),
    path('card',views.card,name='card'),
    path('singerProduct/<int:id>/',views.singerProduct,name='singerProduct'),
    path('singerProduct/<int:id>/edit',views.EditProduct,name='EditProduct'),
    path('singerProduct/<int:id>/delete',views.DeleteProduct,name='DeleteProduct'),
]