from django.urls import path

from papers import views

urlpatterns = [
    path('<str:fk>/',views.paperInfo),
    path('<str:fk>/paperAdd/', views.paperAdd),
    path('<str:fk>/paperEdit/', views.paperEdit),
    path('<str:fk>/paperDel/', views.paperDel),
]