from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('<int:rubric_id>/', views.rubric_bbs),
    # path('', views.index),
]