from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_report'),
    path('bugs/<int:bug_id>/', views.BugDetail.as_view(), name='bug_detail'),
    path('bugs/new/', views.create_bug_report, name='new_bug'),
    path('features/', views.feature_list, name='feature_request'),
    path('features/<int:feature_id>/', views.FeatureDetail.as_view(), name='feature_detail'),
    path('features/new/', views.create_feature_request, name='new_feature'),
]
