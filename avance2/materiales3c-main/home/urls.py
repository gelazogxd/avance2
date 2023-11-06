from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
        path('', views.Index.as_view(), name="index"),
        path('about/', views.About.as_view(), name="about"),
        path('identity', views.Identity.as_view(), name="identity"),
        path('contacto', views.Contacto.as_view(), name="contacto"),
    ]