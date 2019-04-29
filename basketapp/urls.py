from django.conf.urls import url
from django.urls import include, path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path(r'', basketapp.basket, name='view'),
    path(r'add/<int:pk>/', basketapp.basket_add, name='add'),
    path(r'remove/<int:pk>/', basketapp.basket_remove, name='remove'),
    
    path(r'edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]

    