import unittest
from unittest.mock import patch, mock_open
import json

# Импортируйте ваш класс Vacancy и класс JSONFileManager
from src.file_manager import JSONFileManager
from src.vacancy import Vacancy

class TestJSONFileManager(unittest.TestCase):
    def setUp(self):
        self.file_manager = JSONFileManager('test_vacancies.json')

    @patch('builtins.open', new_callable=mock_open)
    def test_add_vacancy(self, mock_file):
        vacancy = Vacancy(title="Программист", url="http://example.com", salary=100000, description="Тестовая вакансия")
        self.file_manager.add_vacancy(vacancy)

        mock_file.assert_called_once_with('test_vacancies.json', 'a', encoding='utf8')
        handle = mock_file()
        handle.write.assert_called_once_with(json.dumps(vacancy.__dict__, ensure_ascii=False) + "\n")

    @patch('builtins.open', new_callable=mock_open, read_data='{"title": "Программист", "url": "http://example.com", "salary": 100000, "description": "Тестовая вакансия"}\n')
    def test_get_vacancies(self, mock_file):
        result = self.file_manager.get_vacancies("Тестовая вакансия")
        expected = [{'title': 'Программист', 'url': 'http://example.com', 'salary': 100000, 'description': 'Тестовая вакансия'}]
        self.assertEqual(result, expected)

    @patch('builtins.open', new_callable=mock_open,
           read_data='{"title": "Программист", "url": "http://example.com", "salary": 100000, "description": "Тестовая вакансия"}\n')
    def test_remove_vacancy(self, mock_file):
        vacancy = Vacancy(title="Программист", url="http://example.com", salary=100000, description="Тестовая вакансия")
        self.file_manager.add_vacancy(vacancy)

        self.file_manager.remove_vacancy(vacancy.id)

        # Проверка, что `open` был вызван для записи
        mock_file.assert_any_call('test_vacancies.json', 'w', encoding='utf8')

        # Проверка чего-либо, связанного с безопасностью записи
        handle = mock_file()
        handle.write.assert_not_called()  # В этом тесте не должно быть записей

if __name__ == '__main__':
    unittest.main()