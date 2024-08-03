from django.urls import path
from . import views

app_name = 'dataentry'
urlpatterns = [
    path('import-data/', views.import_data, name='import_data'),
    path('', views.data_entry_view, name='data_entry_view'),
    path('<int:id>/', views.detail, name='detail')
]