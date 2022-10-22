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