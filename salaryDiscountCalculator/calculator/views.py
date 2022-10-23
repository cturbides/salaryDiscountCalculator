from email.mime import base
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from calculator.calculator import Calculator

@csrf_exempt
def main(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            base_salary = float(body.get('baseSalary'))
        except:
            return JsonResponse({"Error": "Trying to obtain baseSalary"})
        
        base_calculator = Calculator(base_salary)
            
        sfs = base_calculator.sfs()
        afp = base_calculator.afp()
        isr_list = base_calculator.isr()
        net_salary = base_calculator.net_salary()
        
        data = {
            "sfs": sfs,
            "afp": afp,
            "isr": isr_list[0], 
            "isrMessage": isr_list[1],
            "netSalary": net_salary
        }
        
        return JsonResponse(data)
    else:    
        return render(request, 'calculator/index.html')