from unittest import TestCase
from unittest.mock import patch, Mock
from src.API import HH  # Замените на правильный путь к вашему модулю


class TestHHParser(TestCase):

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

        # Проверяем, что сообщение исключения соответствует ожидаемому
        self.assertEqual(str(context.exception), "Ошибка подключения к API: 500")