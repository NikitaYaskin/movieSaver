from django.urls import path

from . import views

app_name = 'moviesaver'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('sections/', views.sections, name='sections'),
    path('films/', views.films, name='films'),
    path('serials/', views.serials, name='serials'),
    path('anime/', views.anime, name='anime'),
    path('cartoons/', views.cartoons, name='cartoons'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
]