from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.power_bi_dashboard, name='power_bi_dashboard'),
    path('ml-prediction/', views.ml_prediction, name='ml_prediction'),
    path('crud/', views.crud_operations, name='crud_operations'),  # List records and show form
    path('crud/<int:sr_no>/', views.crud_operations, name='crud_operations_with_id'),  # Create/update record
    path('crud/delete/<int:sr_no>/', views.delete_record, name='delete_record'),  # Delete record
    path('reports/', views.report_page, name='report_page'),
    path('admin_onboarding/', views.admin_onboarding, name='admin_onboarding'),
    path('secured_section/', views.SecuredSectionView.as_view(), name='secured_section'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('download_excel/', views.download_excel, name='download_excel'),
    path('report/', views.report_page, name='report_page'),

]










# urlpatterns = [
#     path('dashboard/', views.power_bi_dashboard, name='power_bi_dashboard'),
#     path('ml-prediction/', views.ml_prediction, name='ml_prediction'),
#     path('crud/', views.crud_operations, name='crud_operations'),
#     path('crud/delete/<int:sr_no>/', views.delete_record, name='delete_record'),
#     # path('crud_operations/', crud_operations, name='crud_operations'),
#     path('crud_operations/<int:sr_no>/', crud_operations, name='crud_operations_with_id'),

#     path('reports/', views.report_page, name='report_page'),
#     path('admin_onboarding/', views.admin_onboarding, name='admin_onboarding'),
#     # path('secured_section/', views.secured_section, name='secured_section'),  # Add this 
#     path('secured_section/', views.SecuredSectionView.as_view(), name='secured_section'),
#     path('crud/', crud_operations, name='crud_operations'),
#     path('crud/<int:sr_no>/', crud_operations, name='crud_operations_with_id'),
 

# ]
