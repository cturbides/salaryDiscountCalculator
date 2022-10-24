from calculator import Calculator
import unittest # Using the in-built testing framework to make a TDD

class TestGetSFS(unittest.TestCase):
    """
    SFS -> Seguro Familiar de Salud
    Is equal to the 3.04% of the net salary, with a maximun set
        to 4,742.40$ DOP
    """
    def test_salary_of_3k(self):
        salary = Calculator(3e3)
        self.assertEqual(salary.sfs(), 91.2, "Incorrect SFS with base salary of 3K")
    
    def test_salary_of_15k(self):
        salary = Calculator(1.5e4)
        self.assertEqual(salary.sfs(), 456, "Incorrect SFS with base salary of 15K")
    
    def test_salary_of_30k(self):
        salary = Calculator(3e4)
        self.assertEqual(salary.sfs(), 912, "Incorrect SFS with base salary of 30K")
    
    def test_salary_of_60k(self):
        salary = Calculator(6e4)
        self.assertEqual(salary.sfs(), 1824, "Incorrect SFS with base salary of 60K")
    
    def test_salary_of_90k(self):
        salary = Calculator(9e4)
        self.assertEqual(salary.sfs(), 2736, "Incorrect SFS with base salary of 90K")
    
    def test_salary_of_120k(self):
        salary = Calculator(1.2e5)
        self.assertEqual(salary.sfs(), 3648, "Incorrect SFS with base salary of 120K")
        
    def test_salary_of_200k(self):
        salary = Calculator(2e5)
        self.assertEqual(salary.sfs(), 4943.80, "Incorrect SFS with base salary of 200K")
         
class TestGetAFP(unittest.TestCase):
    """
    AFP -> Administradora de Fondo de Pensiones
    Is equal to the 2.87% of the net salary, with a maximun set
        to 8,954.40$ DOP
    """
    def test_salary_of_3k(self):
        salary = Calculator(3e3)
        self.assertEqual(salary.afp(), 86.1, "Incorrect AFP with base salary of 3K")
    
    def test_salary_of_15k(self):
        salary = Calculator(1.5e4)
        self.assertEqual(salary.afp(), 430.5, "Incorrect AFP with base salary of 15K")
    
    def test_salary_of_30k(self):
        salary = Calculator(3e4)
        self.assertEqual(salary.afp(), 861, "Incorrect AFP with base salary of 30K")
    
    def test_salary_of_60k(self):
        salary = Calculator(6e4)
        self.assertEqual(salary.afp(), 1722, "Incorrect AFP with base salary of 60K")
    
    def test_salary_of_90k(self):
        salary = Calculator(9e4)
        self.assertEqual(salary.afp(), 2583, "Incorrect AFP with base salary of 90K")
    
    def test_salary_of_120k(self):
        salary = Calculator(1.2e5)
        self.assertEqual(salary.afp(), 3444, "Incorrect AFP with base salary of 120K")
        
    def test_salary_of_200k(self):
        salary = Calculator(2e5)
        self.assertEqual(salary.afp(), 5740, "Incorrect AFP with base salary of 200K") 

class TestGetISR(unittest.TestCase):
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
    
    def test_salary_of_3k(self):
        salary = Calculator(3e3)
        self.assertEqual(salary.isr()[0], 0, "Incorrect ISR with base salary of 3K")
    
    def test_salary_of_15k(self):
        salary = Calculator(1.5e4)
        self.assertEqual(salary.isr()[0], 0, "Incorrect ISR with base salary of 15K")
    
    def test_salary_of_30k(self):
        salary = Calculator(3e4)
        self.assertEqual(salary.isr()[0], 0, "Incorrect ISR with base salary of 30K")
    
    def test_salary_of_35k(self):
        salary = Calculator(3.5e4)
        self.assertEqual(salary.isr()[0], 0, "Incorrect ISR with base salary of 35K")
    
    def test_salary_of_60k(self):
        salary = Calculator(6e4)
        self.assertEqual(salary.isr()[0], 3486.65, "Incorrect ISR with base salary of 60K")
    
    def test_salary_of_90k(self):
        salary = Calculator(9e4)
        self.assertEqual(salary.isr()[0], 9753.19, "Incorrect ISR with base salary of 90K")
    
    def test_salary_of_120k(self):
        salary = Calculator(1.2e5)
        self.assertEqual(salary.isr()[0], 16809.94, "Incorrect ISR with base salary of 120K")
        
    def test_salary_of_200k(self):
        salary = Calculator(2e5)
        self.assertEqual(salary.isr()[0], 35911.99, "Incorrect ISR with base salary of 200K") 

class TestGetNetSalary(unittest.TestCase):
    """
    NET SALARY -> Worker's real salary
    Consists on the base salary minus SFS minus AFP minus ISR
    """
    def test_salary_of_3k(self):
        salary = Calculator(3e3)
        self.assertEqual(salary.net_salary(), 2822.7, "Incorrect Net Salary with base salary of 3K")
    
    def test_salary_of_15k(self):
        salary = Calculator(1.5e4)
        self.assertEqual(salary.net_salary(), 14113.5, "Incorrect Net Salary with base salary of 15K")
    
    def test_salary_of_30k(self):
        salary = Calculator(3e4)
        self.assertEqual(salary.net_salary(), 28227, "Incorrect Net Salary with base salary of 30K")
    
    def test_salary_of_35k(self):
        salary = Calculator(3.5e4)
        self.assertEqual(salary.net_salary(), 32931.50, "Incorrect Net Salary with base salary of 35K")
    
    def test_salary_of_60k(self):
        salary = Calculator(6e4)
        self.assertEqual(salary.net_salary(), 52967.35, "Incorrect Net Salary with base salary of 60K")
    
    def test_salary_of_90k(self):
        salary = Calculator(9e4)
        self.assertEqual(salary.net_salary(), 74927.81, "Incorrect Net Salary with base salary of 90K")
    
    def test_salary_of_120k(self):
        salary = Calculator(1.2e5)
        self.assertEqual(salary.net_salary(), 96098.06, "Incorrect Net Salary with base salary of 120K")
        
    def test_salary_of_200k(self):
        salary = Calculator(2e5)
        self.assertEqual(salary.net_salary(), 153404.21, "Incorrect Net Salary with base salary of 200K") 

if __name__ == '__main__':
    unittest.main()