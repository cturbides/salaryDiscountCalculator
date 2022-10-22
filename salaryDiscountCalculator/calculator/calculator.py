class Calculator:
    def __init__(self, salary: int):
        self.base_salary = salary
    
    def sfs(self) -> float:
        """
        SFS -> Seguro Familiar de Salud
        Is equal to the 3.04% of the net salary, with a maximun set
            to 4,742.40$ DOP
        """
        
        sfs_amount = (self.base_salary * 3.04)/100
        
        if sfs_amount > 4742.40:
            return 4742.40
        return float(sfs_amount)
    
    def afp(self) -> float:
        """
        AFP -> Administradora de Fondo de Pensiones
        Is equal to the 2.87% of the net salary, with a maximun set
            to 8,954.40$ DOP
        """
        
        afp_amount = (self.base_salary * 2.87)/100
        
        if afp_amount > 8954.40:
            return 8954.40
        return float(afp_amount)
    
    def mensual_isr_calculations(self, anual_salary: float) -> tuple:
        anual_isr_amount, mensual_isr = float(), float()
        message = str()
        
        if anual_salary < 416220:
            mensual_isr = 0
            message = "Anual Salaries less than 416,220$ DOP are exempt."
        elif 416220 < anual_salary < 624329:
            anual_isr_amount = (anual_salary - 416220.01)*.15
            mensual_isr = anual_isr_amount/12
            message = """
            Anual Salaries over 416,220$ DOP and less than 624,329$ DOP
            just have to pay the 15% of the surplus of 416,220.01$ DOP  
            """
        elif 624329 < anual_salary < 867123:
            anual_isr_amount = 31216 + (anual_salary - 624329.01)*.20
            mensual_isr = anual_isr_amount/12
            message = """
            Anual Salaries over 624,329$ DOP and less than 867,123$ DOP
            just have to pay 31,216$ DOP plus the 20% of the surplus of 
            624,329.01$ DOP  
            """
        else:
            anual_isr_amount = 79776 + (anual_salary - 867123.01)*.25
            mensual_isr = anual_isr_amount/12
            message = """
            Anual Salaries over 867,123$ DOP just have to pay 79,776$ DOP
            plus the 25% of the surplus of 867,123.01$ DOP  
            """
            
        return (mensual_isr, message)
    
    def isr(self) -> float:
        """
        ISR -> Impuestos Sobre la Renta
        Apply just for net salaries (monthly) over ~34,667$ DOP.
        To calculate it we must start talking about anual values.
        
        TABLE:
            A.S = Anual Salaries
            
            - 416,220.01 < A.S < 624,329.00 = 15% of (A.S - 416,220.01)
            - 624,329.01 < A.S < 867,123.00 = 31,216 + 20% of (A.S - 624,329.01)
            - 867,123.01 < A.S = 79,776 + 25% of (A.S - 867,123.01)
        """
        
        anual_salary = float(self.base_salary * 12)
        isr_tuple = self.mensual_isr_calculations(anual_salary)
        isr_amount = round(isr_tuple[0], 2)
        
        return isr_amount
    
    def net_salary(self):
        net_salary = self.base_salary - self.sfs() - self.afp() - self.isr()
        net_salary = round(net_salary, 2)
                 
        return net_salary