from calculator import Calculator
import unittest # Using the in-built testing framework to make a TDD

class TestGetSFS(unittest.TestCase):
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
         


if __name__ == '__main__':
    unittest.main()