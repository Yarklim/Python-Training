# ================= Абстракция =================

# Выделение только значимых характеристик объекта и отсечение второстепенных деталей.
# Общая бизнес-логика (код), которую дочерние классы должны переиспользовать.

from abc import ABC, abstractmethod


# 1. Абстрактный класс (контракт)
class NotificationSender(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        """Абстрактный метод. У него нет реализации здесь,

        но он обязует все дочерние классы его реализовать.
        """
        return


# 2. Конкретная реализация для Email (скрываю логику SMTP, подключения и т.д.)
class EmailNotification(NotificationSender):
    def send(self, recipient: str, message: str) -> None:
        # Здесь была бы сложная логика подключения к SMTP-серверу
        print(f'Отправка Email на {recipient}: {message}')


# 3. Конкретная реализация для Telegram (скрываю логику работы с Bot API)
class TelegramNotification(NotificationSender):
    def send(self, recipient: str, message: str) -> None:
        # Здесь была бы сложная логика запросов к Telegram API
        print(f'Отправка Telegram-сообщения для {recipient}: {message}')


# --- Использование ---


# Функция бизнес-логики работает с абстракцией, ей всё равно, какой канал используется
def notify_user(sender: NotificationSender, user: str, text: str):
    # Я использую только то, что гарантирует абстрактный класс
    sender.send(user, text)


# Создаю конкретные реализации
email_service = EmailNotification()
telegram_service = TelegramNotification()

# Передаю в функцию
notify_user(email_service, 'alex@example.com', 'Ваш заказ готов!')
notify_user(telegram_service, '@alex_dev', 'Ваш заказ готов!')
