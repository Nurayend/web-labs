import json
from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def companies_list(request):
    if request.method == "GET":
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'], address=['address'])
        except Exception as e:
            return JsonResponse({'message': str(e)})
        return JsonResponse(company.to_json())

def company_details(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
            return JsonResponse(company.to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

def vacancies_list_by_company(request, company_id):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        vacancies = company.vacancy_set.all()
        vacancies_json = [v.to_json() for v in vacancies]

        return JsonResponse(vacancies_json, safe=False)

def vacancies_list(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)

def vacancy_details(request, vacancy_id):
    if request.method == "GET":
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return JsonResponse(vacancy.to_json())
        except Vacancy.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

def top_ten(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        json_vacancies = [v.to_json() for v in vacancies]
        return JsonResponse(json_vacancies, safe=False)