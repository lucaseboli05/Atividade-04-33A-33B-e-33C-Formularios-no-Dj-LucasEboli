from django.contrib import admin
from django.urls import path
from AppDoLucas import views

urlpatterns = [
  path('', views.home, name='home'),
  path('idolos', views.create_idolo, name='create_idolo'),
  path('idolos/update/<int:id>', views.update_idolo, name='update_idolo'),
  path('idolos/delete/<int:id>', views.delete_idolo, name='delete_idolo'),
  path('exp/create/', views.create_experiencia, name='create_experiencia'),
  path('exp/update/<int:id>/', views.update_experiencia, name='update_experiencia'),
  path('exp/delete/<int:id>/', views.delete_experiencia, name='delete_experiencia'),
  path('admin/', admin.site.urls),
]
