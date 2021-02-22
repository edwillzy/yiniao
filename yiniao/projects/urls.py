from django.urls import path

from projects import views

urlpatterns = [
    path('<str:fk>/',views.projectInfo),
    path('<str:fk>/projectHAdd/', views.projectHAdd),
    path('<str:fk>/projectHEdit/', views.projectHEdit),
    path('<str:fk>/projectHDel/', views.projectHDel),
    path('<str:fk>/projectVAdd/', views.projectVAdd),
    path('<str:fk>/projectVEdit/', views.projectVEdit),
    path('<str:fk>/projectVDel/', views.projectVDel),
]