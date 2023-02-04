from ds import views
from django.urls import path

urlpatterns = [
    path('/ML', views.DSView_ML.as_view(), name='ds_view_ML'),
    path('/Analyse', views.DSView_Analyse.as_view(), name='ds_view_Analyse')
]

# 定义uml取名规则