from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chk_shape', views.checkShape, name='chk_shape'),
]