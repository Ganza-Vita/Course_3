from abc import ABC, abstractmethod
import requests

class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, *args, **kwargs):
        """Метод для получения вакансий по ключевому слову"""
        pass

class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def load_vacancies(self, keyword):
        """Загружает вакансии по ключевому слову"""
        self.params['text'] = keyword
        vacancies = []

        while self.params['page'] < 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)

            if response.status_code == 200:
                vacancies_batch = response.json()['items']
                vacancies.extend(vacancies_batch)
                self.params['page'] += 1
            else:
                raise Exception(f"Ошибка подключения к API: {response.status_code}")

        return vacancies