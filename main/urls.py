from django.urls import path
from . import views 

app_name = "main"

urlpatterns = [
	path('', views.homePage, name="homePage"),
	path('create/', views.createUser, name="create"),
	path('modify<int:pk>/', views.modifyUser, name="modify"),
	path('delete<int:pk>/', views.deleteUser, name="delete"),
]