from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cv/marketing/', views.cv_marketing, name='cv_marketing'),
]
