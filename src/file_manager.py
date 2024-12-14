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
            with open(self.filename, 'a', encoding="utf-8") as file:
                json_data = json.dumps(vacancy.__dict__, ensure_ascii=False)
                file.write(json_data + "\n")
        except Exception as e:
            print(f"Ошибка при добавлении вакансии: {e}")

    def get_vacancies(self, criteria):
        """Получение вакансий из JSON-файла по критериям"""
        vacancies = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    vacancy_data = json.loads(line.strip())
                    if criteria in vacancy_data.get('description', ''):
                        vacancies.append(vacancy_data)
            return vacancies
        except Exception as e:
            print(f"Ошибка при получении вакансий: {e}")
            return []

    def remove_vacancy(self, vacancy_id):
        """Удаление вакансии из файла"""
        vacancies = self.get_vacancies("")  # Получаем все вакансии
        vacancies = [v for v in vacancies if v.get('id') != vacancy_id]  # Фильтруем удаляемую вакансию

        with open(self.filename, 'w', encoding='utf-8') as file:
            for vacancy in vacancies:
                file.write(json.dumps(vacancy, ensure_ascii=False) + "\n")

    def write_vacancies_to_file(self, vacancies):
        """Запись списка вакансий в файл в формате JSON"""
        vacancies_dict = [vacancy.to_dict() for vacancy in vacancies]  # Преобразуем в список словарей
        with open(self.filename, 'w', encoding='utf-8') as f:  # Изменение на self.filename
            json.dump(vacancies_dict, f, ensure_ascii=False, indent=4)