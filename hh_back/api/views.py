from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.http import Http404
# Create your views here.
def company_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        json_companies = [c.to_json() for c in companies]
        return JsonResponse(json_companies, safe=False)
def company_detail(request, id):
    try:
        if request.method == "GET":
            company = Company.objects.get(id = id)
            return JsonResponse(company.to_json())
    except Company.DoesNotExist as e:
        return JsonResponse({'error': 'there is no such company '})
def vacancy_by_company(request, id):
    try:
        if request.method == "GET":
            vacancies = Vacancy.objects.filter(company = id)
            json_vacancies_by_company = [v.to_json() for v in vacancies]
            return JsonResponse(json_vacancies_by_company, safe = False)
    except:
        return JsonResponse({'error': 'No vacancies in the company'})
def vacancy_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        json_vacancies = [v.to_json() for v in vacancies]
        return JsonResponse(json_vacancies, safe = False)
def vacancy_detail(request, id):
    try:
        if request.method == "GET":
           vacancy = Vacancy.objects.get(id = id)
           return JsonResponse(vacancy.to_json())
    except:
        return JsonResponse({'error': 'No vacancies with this id'})
def top_ten(request):
    if request.method == "GET":
        vacancy_list_ten = Vacancy.objects.all().order_by('-salary')[:10]
        json_vacancy_list_ten = [v.to_json() for v in vacancy_list_ten]
        return JsonResponse(json_vacancy_list_ten, safe = False)