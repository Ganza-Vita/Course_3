class Vacancy:
    """Класс для хранения информации о вакансии"""

    def __init__(self, title: str, url: str, salary: float, description: str):
        self.title = title
        self.url = url
        self.salary = salary if salary is not None else 0
        self.description = description
        self.validate_salary()

    def validate_salary(self):
        """Проверка валидности зарплаты"""
        if self.salary < 0:
            self.salary = 0  # Устанавливаем зарплату по умолчанию

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __repr__(self):
        return f"Vacancy(title='{self.title}', url='{self.url}', salary={self.salary}, description='{self.description}')"
