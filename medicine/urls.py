from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
path('submit_order/', views.submit_order, name='submit_order'),

    path('order/', views.medicine_order, name='medicine_order'),
    path('search/', views.search_medicine, name='search_medicine'),
    path('medicine/<int:id>/', views.medicine_detail_view, name='medicine_detail'),

]


