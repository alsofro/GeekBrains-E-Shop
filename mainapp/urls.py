from django.conf.urls import url
from django.urls import include, path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
    
    path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),

]

    