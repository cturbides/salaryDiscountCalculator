class Calculator:
    def __init__(self, salary: int):
        self.base_salary = salary
    
    def sfs(self):
        sfs_amount = (self.base_salary * 3.04)/100
        
        if sfs_amount > 4742.40:
            return 4742.40
        return sfs_amount
    