from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.Contact,name='contact'),
    path('showAll',views.showAll,name='showAll'),
    path('<str:Type>',views.Type,name='Type'),
    path('<str:Type>/<int:id>/',views.singerProduct,name='singerProduct'), 
    path('manager/',views.manager,name='manager'),
    path('<int:id>/edit',views.EditProduct,name='EditProduct'),
    path('s<int:id>/delete',views.DeleteProduct,name='DeleteProduct'),
    path('Add/',views.AddProduct,name='AddProduct'),
]