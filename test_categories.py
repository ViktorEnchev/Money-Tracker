import unittest
from categories import Category, Income, Expense


class testCategories(unittest.TestCase):
    def setUp(self):
        self.cat1 = Category('20', 'Food')
        self.cat2 = Category(30, 'Bus')
        self.inc1 = Income(100, 'Beta', "New Income\n")
        self.exp1 = Expense(20, 'Food', 'New Expense\n')

    def test_category(self):
        with self.assertRaises(ValueError):
            Category(-10, 'Unbalibable')
        self.assertEqual(str(self.cat1), '20, Food')
        self.assertEqual(self.cat1 == self.cat2, False)
        with self.assertRaises(TypeError):
            Category('asd', 'bad idea')

    def test_income(self):
        self.assertEqual(str(self.inc1), '100, Beta, New Income\n')
        with self.assertRaises(ValueError):
            Income(-20, 'Unamaginable salary', 'New Income\n')
        with self.assertRaises(TypeError):
            Income(20, 'Salary', 'New Expense\n')

    def test_expense(self):
        self.assertEqual(str(self.exp1), '20, Food, New Expense\n')
        with self.assertRaises(ValueError):
            Expense(-20, 'Lucky thing', 'New Expense\n')
        with self.assertRaises(TypeError):
            Expense(20, 'Salary', 'New Income\n')


if __name__ == '__main__':
    unittest.main()
