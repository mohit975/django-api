from django.http import JsonResponse
# from .models import windapi
# from .serializers import DrinkSerializer
import os
import webbrowser
from rest_framework.decorators import api_view
import subprocess

def execute_bash_command(command):
  result = subprocess.run(command, shell=True, capture_output=True, text=True)
  return result.stdout

@api_view(['GET','POST'])
def run_command(request):
    if request.method == 'POST':
        print('This is sample test')
        # os.popen("mkdir 'C://Users//acer//Desktop//Github//GK KT//api//xyz'")
        output = execute_bash_command("mkdir -p C:/Users/acer/Desktop/Github/GK KT/api/xyz")
        print(output)
        return JsonResponse({'response':'200','method':'post'},safe=False) 
    

    if request.method == 'GET':
        print('This is get request')
        return JsonResponse({'response':'200','method':'get'},safe=False) 
