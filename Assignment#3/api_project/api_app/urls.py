from django.contrib import admin
from django.urls import path


from api_app import views

urlpatterns =[
    path('data/',views.fetch_data,name='fetch_data'),

]
