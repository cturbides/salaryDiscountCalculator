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
        self.assertEqual(salary.sfs(), 91.2, "Incorrect SFS with 3K")
    
    def test_salary_of_15k(self):
        salary = Calculator(1.5e4)
        self.assertEqual(salary.sfs(), 456, "Incorrect SFS with 15K")
    
    def test_salary_of_30k(self):
        salary = Calculator(3e4)
        self.assertEqual(salary.sfs(), 912, "Incorrect SFS with 30K")
    
    def test_salary_of_60k(self):
        salary = Calculator(6e4)
        self.assertEqual(salary.sfs(), 1824, "Incorrect SFS with 60K")
    
    def test_salary_of_90k(self):
        salary = Calculator(9e4)
        self.assertEqual(salary.sfs(), 2736, "Incorrect SFS with 90K")
    
    def test_salary_of_120k(self):
        salary = Calculator(1.2e5)
        self.assertEqual(salary.sfs(), 3648, "Incorrect SFS with 120K")
        
    def test_salary_of_200k(self):
        salary = Calculator(2e5)
        self.assertEqual(salary.sfs(), 4742.40, "Incorrect SFS with 200K")
         
class TestGetAFP(unittest.TestCase):
    """
    AFP -> Administradora de Fondo de Pensiones
    Is equal to the 2.87% of the net salary, with a maximun set
        to 8,954.40$ DOP
    """
    def test_salary_of_3k(self):
        salary = Calculator(3e3)
        self.assertEqual(salary.afp(), 86.1, "Incorrect AFP with 3K")
    
    def test_salary_of_15k(self):
        salary = Calculator(1.5e4)
        self.assertEqual(salary.afp(), 430.5, "Incorrect AFP with 15K")
    
    def test_salary_of_30k(self):
        salary = Calculator(3e4)
        self.assertEqual(salary.afp(), 861, "Incorrect AFP with 30K")
    
    def test_salary_of_60k(self):
        salary = Calculator(6e4)
        self.assertEqual(salary.afp(), 1722, "Incorrect AFP with 60K")
    
    def test_salary_of_90k(self):
        salary = Calculator(9e4)
        self.assertEqual(salary.afp(), 2583, "Incorrect AFP with 90K")
    
    def test_salary_of_120k(self):
        salary = Calculator(1.2e5)
        self.assertEqual(salary.afp(), 3444, "Incorrect AFP with 120K")
        
    def test_salary_of_200k(self):
        salary = Calculator(2e5)
        self.assertEqual(salary.afp(), 5740, "Incorrect AFP with 200K") 


if __name__ == '__main__':
    unittest.main()