# ================= Наследование =================


class Employee:
    def __init__(self, name: str, task: str, salary: float):
        self.name = name
        self.task = task
        self.salary = salary

    def work(self):
        print(f'{self.name} does {self.task}')


class Developer(Employee):
    def __init__(self, name: str, task: str, salary: float, language: str):
        # Вызываем конструктор родительского класса Employee
        super().__init__(name, task, salary)
        self.language = language


class Designer(Employee):
    def __init__(self, name: str, task: str, salary: float, tools: list):
        super().__init__(name, task, salary)
        self.tools = tools


class Tester(Employee):
    # Переопределяем метод work() для тестировщика
    def work(self):
        print(f'{self.name} is testing code')


# Передаем все необходимые аргументы при создании объектов:
frontend_developer = Developer('Alex', 'develop UI', 4000, 'TS')
designer = Designer('Elena', 'create mockups', 3500, ['Figma', 'Photoshop'])
tester = Tester('Max', 'testing', 3000)

# Вызов метода:
tester.work()  # Выведет: Max is testing code
