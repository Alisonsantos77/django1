from . import views
from django.urls import include, path


urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('logout/', views.logout_view, name='logout'),
]
