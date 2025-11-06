from django.urls import path

from todos import views



urlpatterns = [
  path('addTask/' , views.addTask, name='addTask')
]

