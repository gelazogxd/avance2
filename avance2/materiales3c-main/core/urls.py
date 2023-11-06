from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path('list/grantgoal/', views.ListGrantGoal.as_view(), name="gg_list"), 
    #en path se utilizan siempre 3 parametros
]