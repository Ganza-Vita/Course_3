from abc import ABC, abstractmethod
import json

class FileManagerBase(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        """Метод для получения вакансий из файла по критериям"""
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        """Метод для удаления вакансии из файла"""
        pass




class JSONFileManager(FileManagerBase):
    def __init__(self, filename: str = 'vacancies.json'):
        self.filename = filename

    def add_vacancy(self, vacancy):
        """Добавление вакансии в JSON-файл"""
        try:
            with open(self.filename, 'a') as file:
                json_data = json.dumps(vacancy.__dict__)
                file.write(json_data + "\n")
        except Exception as e:
            print(f"Ошибка при добавлении вакансии: {e}")

    def get_vacancies(self, criteria):
        """Получение вакансий из JSON-файла по критериям"""
        vacancies = []
        try:
            with open(self.filename, 'r') as file:
                for line in file.readlines():
                    vacancy_data = json.loads(line.strip())
                    if criteria in vacancy_data.get('description', ''):
                        vacancies.append(vacancy_data)
            return vacancies
        except Exception as e:
            print(f"Ошибка при получении вакансий: {e}")
            return []

    def remove_vacancy(self, vacancy_id):
        """Заглушка для удаления вакансии из файла"""
        pass

    def write_vacancies_to_file(self, vacancies, filename='output_vacancies.txt'):
        """Записывает вакансии в текстовый файл."""
        with open(filename, 'w', encoding='utf-8') as file:
            for vacancy in vacancies:
                file.write(f"{vacancy.title} (Ссылка: {vacancy.url}, Зарплата: {vacancy.salary})\n")
        print(f'Вакансии записаны в файл {filename}.')