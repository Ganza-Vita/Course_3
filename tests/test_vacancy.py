import unittest
from src.vacancy import Vacancy
class TestVacancy(unittest.TestCase):

    def setUp(self):
        """Создание экземпляра Vacancy для тестов"""
        self.vacancy = Vacancy(
            vacancy_id='1',
            title='Программист',
            url='http://example.com',
            salary=100000,
            description='Тестовая вакансия'
        )

    def test_initialization(self):
        """Тест для проверки корректности инициализации"""
        self.assertEqual(self.vacancy.id, '1')
        self.assertEqual(self.vacancy.title, 'Программист')
        self.assertEqual(self.vacancy.url, 'http://example.com')
        self.assertEqual(self.vacancy.salary, 100000)
        self.assertEqual(self.vacancy.description, 'Тестовая вакансия')

    def test_validate_salary(self):
        """Тест для проверки валидации зарплаты"""
        vacancy_with_negative_salary = Vacancy(
            vacancy_id='2',
            title='Тест',
            url='http://example.com',
            salary=-50000,
            description='Тестовая вакансия с отрицательной зарплатой'
        )
        self.assertEqual(vacancy_with_negative_salary.salary, 0)

    def test_to_dict(self):
        """Тест для проверки метода to_dict"""
        expected_dict = {
            'id': '1',
            'title': 'Программист',
            'url': 'http://example.com',
            'salary': 100000,
            'description': 'Тестовая вакансия'
        }
        self.assertEqual(self.vacancy.to_dict(), expected_dict)

    def test_repr(self):
        """Тест для проверки корректности вывода repr"""
        expected_repr = "Vacancy(id='1', title='Программист', url='http://example.com', salary=100000, description='Тестовая вакансия')"
        self.assertEqual(repr(self.vacancy), expected_repr)
