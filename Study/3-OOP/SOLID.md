# ======================= SOLID =========================

**S** - Single Responsibility Principle (Принцип единственной ответственности) - у класса должна быть только одна причина для изменения.

**O** - Open/Closed Principle (Принцип открытости/закрытости) - программные сущности должны быть открыты для расширения, но закрыты для модификации.

**L** - Liskov Substitution Principle (Принцип подстановки Барбары Лисков) - объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения правильности работы программы.

**I** - Interface Segregation Principle (Принцип разделения интерфейсов) - клиенты не должны зависеть от методов, которые они не используют (лучше много специализированных интерфейсов, чем один общий).

**D** - Dependency Inversion Principle (Принцип инверсии зависимостей) - зависимости должны строиться на абстракциях, а не на конкретных реализациях.

Давайте разберем каждый принцип **SOLID** на практических примерах на Python. Для чистоты кода будем использовать встроенный модуль `abc` (Abstract Base Classes) и аннотации типов.

---

### 1. S - Single Responsibility Principle (Принцип единственной ответственности)

> **У класса должна быть только одна причина для изменения.**

*Суть:* Класс должен решать ровно одну задачу. Если в классе перемешана бизнес-логика, работа с базой данных и отправка уведомлений, его нужно разделить.

**Пример:**

```python
# ❌ Плохо: Класс и сохраняет пользователя, и отправляет email
class UserRegistration:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def save_to_database(self):
        print(f"Сохранение {self.username} в БД...")

    def send_welcome_email(self):
        print(f"Отправка письма на {self.email}...")

# ✅ Хорошо: Ответственности разделены
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class UserRepository:
    def save(self, user: User):
        print(f"Сохранение {user.username} в БД...")

class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Отправка письма на {user.email}...")

```

---

### 2. O - Open/Closed Principle (Принцип открытости/закрытости)

> **Программные сущности должны быть открыты для расширения, но закрыты для модификации.**

*Суть:* Вы должны иметь возможность добавлять новый функционал, не меняя уже существующий проверенный код (обычно через полиморфизм и абстракции).

**Пример:**

```python
from abc import ABC, abstractmethod

# Абстрактный класс оплаты
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# Конкретная реализация 1
class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Оплата {amount} через Stripe.")

# Конкретная реализация 2 (добавили новый способ без изменения старого кода)
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Оплата {amount} через PayPal.")

```

---

### 3. L - Liskov Substitution Principle (Принцип подстановки Барбары Лисков)

> **Объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения правильности работы программы.**

*Суть:* Дочерний класс не должен ломать поведение родительского класса. Если функция ожидает базовый класс, она должна корректно работать с любым его наследником.

**Пример:**

```python
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Лечу в небе!")

class Penguin(Bird):
    # Пингвин не летает, но он передвигается (не ломает контракт базового класса)
    def move(self):
        print("Иду по льду!")

```

---

### 4. I - Interface Segregation Principle (Принцип разделения интерфейсов)

> **Клиенты не должны зависеть от методов, которые они не используют.**

*Суть:* Лучше создать много маленьких специализированных интерфейсов (абстрактных классов), чем один огромный универсальный.

**Пример:**

```python
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Обычный принтер реализует только то, что умеет
class SimplePrinter(Printer):
    def print_document(self):
        print("Печать документа...")

# МФУ реализует оба интерфейса
class MultiFunctionDevice(Printer, Scanner):
    def print_document(self):
        print("Печать...")

    def scan_document(self):
        print("Сканирование...")

```

---

### 5. D - Dependency Inversion Principle (Принцип инверсии зависимостей)

> **Зависимости должны строиться на абстракциях, а не на конкретных реализациях.**

*Суть:* Модули верхних уровней не должны зависеть от модулей нижних уровней. Оба должны зависеть от абстракций. В Python это обычно достигается через внедрение зависимостей (Dependency Injection).

**Пример:**

```python
# Абстракция
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Низкоуровневая реализация
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[LOG]: {message}")

# Высокоуровневый модуль зависит от абстракции, а не от конкретного логгера
class OrderService:
    def __init__(self, logger: Logger):
        self.logger = logger  # Внедрение зависимости через конструктор

    def create_order(self):
        # Бизнес-логика...
        self.logger.log("Заказ успешно создан!")

```

---

Какой из этих принципов на практике вызывает у вас больше всего вопросов или чаще всего нарушается в существующих проектах?