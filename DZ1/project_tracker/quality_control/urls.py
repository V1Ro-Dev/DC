from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='quality_control'),
    path('bugs/', views.bug_list, name='bug_report'),
    path('features/', views.feature_list, name='feature_request'),
    path('bug/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('feature/<int:feature_id>/', views.feature_detail, name='feature_detail')
]
