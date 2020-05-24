from django.contrib import admin
from django.urls import path
from vote import views

urlpatterns = [
    path('', views.show_subjects, name='index'),
    #path('show_subjects', views.show_subjects, name='show_subjects'),
    path('teachers/', views.show_teachers, name='show_teachers'),
    path('praise/', views.praise_or_criticize),
    path('criticize/', views.praise_or_criticize),
    path('admin/', admin.site.urls),
]

