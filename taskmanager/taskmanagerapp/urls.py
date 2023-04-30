from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('login', views.head_login, name="login"),
    path('manager_login', views.manager_login, name="manager_login"),
    path('staff_login', views.staff_login, name="staff_login"),
    path('teamlead_login', views.teamlead_login, name="teamlead_login"),

    path('user_login', views.user_login, name="user_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('manager_dashboard', views.manager_dashboard, name="manager_dashboard"),
    path('staff_dashboard', views.staff_dashboard, name="staff_dashboard"),
    path('teamlead_dashboard', views.teamlead_dashboard, name="teamlead_dashboard"),

    path('dashboard1', views.dashboard1, name="dashboard1"),
    path('create-task', views.createTask, name="create-task"),
    path('manager_create-task', views.manager_createTask, name="manager_create-task"),
    path('staff_create-task', views.staff_createTask, name="staff_create-task"),
    path('teamlead_create-task', views.teamlead_createTask, name="teamlead_create-task"),
    path('view-tasks', views.viewTask, name="view-tasks"),
    path('staff_view-tasks', views.staff_viewTask, name="staff_view-tasks"),
    path('teamlead_view-tasks', views.teamlead_viewTask, name="teamlead_view-tasks"),
    path('manager_view-tasks', views.manager_viewTask, name="manager_view-tasks"),

    path('view-tasks1', views.viewTask1, name="view-tasks1"),
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    path('user-logout', views.user_logout, name="user-logout"),
]
