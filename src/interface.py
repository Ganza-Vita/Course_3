from src.API import HH
from src.vacancy import Vacancy
from src.file_manager import JSONFileManager


def user_interface():
    api = HH()
    file_manager = JSONFileManager()

    api.connect()
    search_keyword = input("Введите поисковый запрос для вакансий: ")
    top_n = int(input("Введите количество вакансий по зарплате (N): "))

    vacancies_data = api.load_vacancies(search_keyword)
    vacancies = []

    for data in vacancies_data:
        title = data.get('name')
        url = data.get('alternate_url')
        salary = data.get('salary')

        salary_value = salary.get('from', 0) if salary is not None else 0
        description = data.get('description', '')

        vacancy = Vacancy(title, url, salary_value, description)
        file_manager.add_vacancy(vacancy)
        vacancies.append(vacancy)

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
        print(f"- {v['title']} (Ссылка: {v['url']}, Зарплата: {v['salary']})")

    # Записываем вакансия с ключевым словом в файл
    file_manager.write_vacancies_to_file(matching_vacancies)