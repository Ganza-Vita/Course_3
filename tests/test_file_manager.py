import unittest
import json
import os

from src.file_manager import JSONFileManager

class TestMyJSONFileManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Запуск перед всеми тестами. Создание тестового файла."""
        cls.test_filename = 'test_vacancies.json'
        cls.manager = JSONFileManager(filename=cls.test_filename)

    @classmethod
    def tearDownClass(cls):
        """Запуск после всех тестов. Удаление тестового файла."""
        if os.path.exists(cls.test_filename):
            os.remove(cls.test_filename)

    def test_add_vacancy(self):
        """Тест для проверки добавления вакансий."""
        vacancy = {'id': 1, 'title': 'Программист', 'salary': 100000}
        self.manager.add_vacancy(vacancy)

        # Проверяем, что вакансии добавлены правильно
        with open(self.test_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0], vacancy)

    def test_remove_vacancy(self):
        """Тест для проверки удаления вакансий."""
        vacancy1 = {'id': 1, 'title': 'Программист', 'salary': 100000}
        vacancy2 = {'id': 2, 'title': 'Дизайнер', 'salary': 80000}
        self.manager.add_vacancy(vacancy1)
        self.manager.add_vacancy(vacancy2)

        # Удаляем первую вакансию
        self.manager.remove_vacancy(1)

        # Проверяем, что осталась только вторая вакансия
        with open(self.test_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0], vacancy2)

    def test_get_vacancies(self):
        """Тест для проверки получения всех вакансий."""
        vacancy = {'id': 3, 'title': 'Тестировщик', 'salary': 90000}
        self.manager.add_vacancy(vacancy)

        vacancies = self.manager.get_vacancies("")
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0], vacancy)
