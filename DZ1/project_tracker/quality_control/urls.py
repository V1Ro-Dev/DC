from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='quality_control'),
    path('bugs/', views.bug_list, name='bug_report'),
    path('features/', views.feature_list, name='feature_request'),
    path('bugs/<int:bug_id>/', views.BugDetail.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetail.as_view(), name='feature_detail')
]
