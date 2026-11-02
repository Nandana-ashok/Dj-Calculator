from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class AdditionView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 + n2
        # print(request_body)
        data = {
            'Sum': result
        }
        return JsonResponse(data)
@method_decorator(csrf_exempt,name='dispatch')
class SubtractionView(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        difference = n1 - n2
        result = {
            'Difference': difference
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        n1 = form.get('num1')
        n2 = form.get('num2')
        product = n1 * n2
        result = {
            "Product": product
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class DivisionView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        n1 = form.get('num1')
        n2 = form.get('num2')
        division = n1 / n2
        result = {
            "Division" :division
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class RemainderView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        n1 = form.get('num1')
        n2 = form.get('num2')
        remainder = n1 % n2
        result = {
            "Remainder":remainder
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class PercentageView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        mark = form.get('obtained_mark')
        total = form.get('total_mark')
        percentage = (mark / total)*100
        result = {
            "Pecentage":percentage
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class BmiView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        height = form.get('height')
        weight = form.get('weight')
        bmi = weight / (height/100)**2
        result = {
            "BMI":bmi
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class AreaView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        l = form.get('length')
        h = form.get('height')
        area = l*h
        result = {
            "Area":area
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class AgeView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        b = form.get('birth-year')
        c = form.get('current-year')
        age = c-b
        result = {
            "AGE":age
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterestView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        p = form.get('principle')
        t = form.get('time')
        r = form.get('rate')
        si = (p*t*r)/100
        result = {
            "Principle":p,
            "Rate":r,
            "Time":t,
            "Simple-Interest":si
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class ElectricityView(View):
    def post(self,request):
        data = request.body
        form = loads(data)
        unit = form.get('unit')
        rate = form.get('rate')
        bill = unit * rate
        result = {
            "Unit":unit,
            "Rate":rate,
            "Bill":bill
        }
        return JsonResponse(result)