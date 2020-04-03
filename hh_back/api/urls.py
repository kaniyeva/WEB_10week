from django.urls import path
from api import views

urlpatterns = [
    path('', views.company_list),
    path('companies/', views.company_list),
    path('companies/<int:id>/', views.company_detail),
    path('companies/<int:id>/vacancies/', views.vacancy_by_company),
    path('vacancies/', views.vacancy_list),
    path('vacancies/<int:id>/', views.vacancy_detail),
    path('vacancies/top_ten/', views.top_ten)
]