from django.urls import path

from baseInfo import views

urlpatterns = [
    path('<str:pk>/',views.baseInfo),
    path('<str:pk>/personInfoEdit/', views.personInfoEdit),
    path('<str:pk>/eduExpAdd/', views.eduExpAdd),
    path('<str:pk1>/eduExpEdit/', views.eduExpEdit),
    path('<str:pk1>/eduExpDel/', views.eduExpDel),
    path('<str:pk>/workExpAdd/', views.workExpAdd),
    path('<str:pk1>/workExpEdit/', views.workExpEdit),
    path('<str:pk1>/workExpDel/', views.workExpDel),
    path('<str:pk>/posiExpAdd/', views.posiExpAdd),
    path('<str:pk1>/posiExpEdit/', views.posiExpEdit),
    path('<str:pk1>/posiExpDel/', views.posiExpDel),
    path('<str:pk>/partEdit/', views.partEdit),
    path('<str:pk>/myTeachingAdd/', views.myTeachingAdd),
    path('<str:pk1>/myTeachingEdit/', views.myTeachingEdit),
    path('<str:pk1>/myTeachingDel/', views.myTeachingDel),

]