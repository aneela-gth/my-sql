# from django.shortcuts import render

# # Create your views here.
from django .http import JsonResponse
import json 
def student_api(request):
  if request.methrod=='GET':
    data={
      "name":"aneela",
      "course":"python",
      "age":21
    }
    return JsonResponse(data)