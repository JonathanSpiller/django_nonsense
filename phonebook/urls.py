from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('home/<int:number>', views.home, name='home'),
    path('persons/', views.persons, name='persons'),
    path('person/<int:id>', views.person, name='person'),
    path('add_person/', views.add_person, name='add_person'),

]
