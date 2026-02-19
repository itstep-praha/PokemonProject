from django.urls import path
from test_app import views


urlpatterns = [
    path('my-site/', views.my_site_view),
    path('my-json/', views.my_json_view),
    path('my-template/', views.my_template_view),
    path('my-name/<str:name>/', views.my_name_view),
    path('my-user/<int:user_id>/', views.my_user_view),
]
