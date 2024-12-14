import unittest
from unittest.mock import patch, Mock
from src.API import HH


class TestHHParser(unittest.TestCase):

    @patch('requests.get')  # Мокаем requests.get
    def test_load_vacancies(self, mock_get):
        # Создаем мок-ответ и устанавливаем его как возвращаемое значение для метода get()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [
                {'id': '1', 'name': 'Вакансия 1'},
                {'id': '2', 'name': 'Вакансия 2'}
            ]
        }
        mock_get.return_value = mock_response

        # Создаем экземпляр нашего класса
        hh_parser = HH()

        # Вызываем метод загрузки вакансий
        vacancies = hh_parser.load_vacancies('Python')

        # Проверяем, что вакансии вернулись корректно
        self.assertEqual(len(vacancies), 2)  # Должно быть 2 вакансии
        self.assertEqual(vacancies[0]['name'], 'Вакансия 1')  # Проверяем первую вакансию
        self.assertEqual(vacancies[1]['name'], 'Вакансия 2')  # Проверяем вторую вакансию

        # Убедимся, что метод requests.get был вызван
        self.assertTrue(mock_get.called)

    @patch('requests.get')  # Мокаем requests.get
    def test_load_vacancies_api_error(self, mock_get):
        # Настраиваем мок, чтобы он возвращал ошибку
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        hh_parser = HH()

        # Проверяем, что при ошибке API вызывается исключение
        with self.assertRaises(Exception) as context:
            hh_parser.load_vacancies('Python')

        self.assertEqual(str(context.exception), "Ошибка подключения к API: 500")
