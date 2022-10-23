from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from calculator.calculator import Calculator

@csrf_exempt
def main(request):
    if request.method == 'POST':
        base_salary, bonifications, extra_hours = float(), 0.0, 0.0
        print(request.body)
        body = json.loads(request.body)
        base_salary = float(body.get('baseSalary'))
            
        if body.get('bonifications'):
            bonifications = float(body.get('bonifications'))
        if body.get('extraHours'):
            extra_hours = float(body.get('extraHours'))
        
        
        base_calculator = Calculator(base_salary, bonifications=bonifications, extra_hours=extra_hours)
            
        sfs = base_calculator.sfs()
        afp = base_calculator.afp()
        isr_list = base_calculator.isr()
        retentions = base_calculator.retentions()
        net_salary = base_calculator.net_salary()
        
        data = {
            "baseSalary": base_salary,
            "extraHours": extra_hours,
            "bonifications": bonifications,
            "sfs": sfs,
            "afp": afp,
            "isr": isr_list[0], 
            "isrMessage": isr_list[1],
            "retentions": retentions,
            "netSalary": net_salary
        }
        
        return JsonResponse(data)
    else:    
        return render(request, 'calculator/index.html')