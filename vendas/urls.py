from django.urls import path
from . import views


urlpatterns = [
    path('', views.nova_venda, name='nova_venda'),
    path('lista/', views.lista, name='lista'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]
