"""
URL configuration for todoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from todoApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('new/', views.todo_create, name='todo_create'),
    path('<int:pk>/edit/', views.todo_update, name='todo_update'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('<int:pk>/update-status/', views.todo_update_status, name='todo_update_status'),
    path('search/',views.todo_search, name='todo_search'),
]
