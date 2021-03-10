from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('ty_pidor', views.huindex, name="about")
    # path('about', views.huindex, name="about")
]
