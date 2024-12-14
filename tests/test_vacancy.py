import unittest
from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_initialization(self):
        """Тест корректной инициализации вакансии"""
        vacancy = Vacancy(title='Программист', url='http://example.com', salary=100000, description='Тестовая вакансия')
        self.assertEqual(vacancy.title, 'Программист')
        self.assertEqual(vacancy.url, 'http://example.com')
        self.assertEqual(vacancy.salary, 100000)
        self.assertEqual(vacancy.description, 'Тестовая вакансия')

    def test_salary_validation_positive(self):
        """Тест на установку положительной зарплаты"""
        vacancy = Vacancy(title='Программист', url='http://example.com', salary=50000, description='Тестовая вакансия')
        self.assertEqual(vacancy.salary, 50000)

    def test_salary_validation_negative(self):
        """Тест на установку отрицательной зарплаты"""
        vacancy = Vacancy(title='Программист', url='http://example.com', salary=-10000, description='Тестовая вакансия')
        self.assertEqual(vacancy.salary, 0)  # Зарплата должна быть установлена в 0

    def test_less_than_operator(self):
        """Тест для проверки оператора < для зарплат"""
        vacancy1 = Vacancy(title='Программист', url='http://example.com', salary=50000, description='Тестовая вакансия')
        vacancy2 = Vacancy(title='Дизайнер', url='http://example.com', salary=60000, description='Тестовая вакансия')
        self.assertTrue(vacancy1 < vacancy2)  # Должно быть True

    def test_greater_than_operator(self):
        """Тест для проверки оператора > для зарплат"""
        vacancy1 = Vacancy(title='Программист', url='http://example.com', salary=60000, description='Тестовая вакансия')
        vacancy2 = Vacancy(title='Дизайнер', url='http://example.com', salary=50000, description='Тестовая вакансия')
        self.assertTrue(vacancy1 > vacancy2)  # Должно быть True

    def test_repr(self):
        """Тест для проверки корректности вывода repr"""
        vacancy = Vacancy(title='Программист', url='http://example.com', salary=100000, description='Тестовая вакансия')
        expected_repr = "Vacancy(title='Программист', url='http://example.com', salary=100000, description='Тестовая вакансия')"
        self.assertEqual(repr(vacancy), expected_repr)
