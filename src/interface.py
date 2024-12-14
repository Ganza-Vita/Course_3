from src.API import HH
from src.vacancy import Vacancy
from src.file_manager import JSONFileManager


def user_interface():
    api = HH()
    file_manager = JSONFileManager()

    # api.connect()
    search_keyword = input("Введите поисковый запрос для вакансий: ")
    top_n = int(input("Введите количество вакансий по зарплате (N): "))

    vacancies_data = api.load_vacancies(search_keyword)
    vacancies = []

    # Инициализируем уникальный идентификатор
    id_counter = 1

    for data in vacancies_data:
        title = data.get('name')
        url = data.get('alternate_url')
        salary = data.get('salary')

        # Обработка зарплат
        salary_value = salary['from'] if salary and 'from' in salary else (
            salary['to'] if salary and 'to' in salary else 0)
        description = data.get('description', '')

        # Создаем экземпляр Vacancy
        vacancy = Vacancy(title, url, salary_value, description, str(id_counter))
        file_manager.add_vacancy(vacancy)
        vacancies.append(vacancy)

        # Увеличиваем счетчик уникальных идентификаторов
        id_counter += 1

    # Сортировка по зарплате
    top_vacancies = sorted(vacancies, key=lambda v: v.salary, reverse=True)[:top_n]
    print("Топ вакансий по зарплате:")
    for v in top_vacancies:
        print(f"- {v.title} (Ссылка: {v.url}, Зарплата: {v.salary})")

    # Записываем топ вакансий в файл
    file_manager.write_vacancies_to_file(top_vacancies)

    keyword_in_description = input("Введите ключевое слово для поиска в описании: ")
    matching_vacancies = file_manager.get_vacancies(keyword_in_description)

    print("Вакансии с ключевым словом в описании:")
    for v in matching_vacancies:
        print(f"- {v.title} (Ссылка: {v.url}, Зарплата: {v.salary})")

