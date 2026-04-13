# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# # Create your views here.
# def home(request):
#     return HttpResponse("welcome to pyhton page")
# from django.http import JsonResponse
# def home(request):
#     data={
#         "name":"ane",
#             "age":21    }
#     return JsonResponse(data)

# from django.db import modeles
# from django.http import JsonResponse
# def home(request):
#     data={
#         "name":"akhi",
#         "age":20,
#         "course":"python",
#         "city":"hyd"
#     }
#     return JsonResponse(data)
# from django.http import HttpResponse
from django.http import JsonResponse
# import json
# products=[]
# def add(request):
#     if request.metod=='POST':
#         name=request.POST.get("name")
#         price=request.POST.get("price")
#         products={
#             "id":len(products)+1,
#             "name":"laptop",
#             "price":20000,
#         }
#         products.append(products)
#         return HttpResponse("produc created succeffully")
#     return HttpResponse("send post request")
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def students(request):
    if request.method=="GET":
        student_data=student.objects.all()
        data=[]
        for student in student_data:
            data.append({
               'name': student.name,
                'age': student.age,
            })
        return JsonResponse(data,safe=False)

# def students(request):
#     return JsonResponse({
#         "name": "aneela",
#         "age": 21
#     })


