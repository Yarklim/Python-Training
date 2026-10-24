# ================= Полиморфизм =================

# Возможность использовать единый интерфейс для работы с сущностями разных типов.

from typing import Protocol


# Определяю протокол (контракт)
class Workable(Protocol):
    def work(self):
        pass


class Developer:
    def work(self):
        print('Writing code')


class Designer:
    def work(self):
        print('Doing design')


# Указываю тип
team: list[Workable] = [Developer(), Designer()]

for member in team:
    member.work()
