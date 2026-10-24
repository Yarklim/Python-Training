from pathlib import Path

# Получаю путь к папке, где лежит текущий .py скрипт
BASE_DIR = Path(__file__).resolve().parent

# Строю точный путь к файлу
file_path = BASE_DIR / 'data' / 'one.txt'

# На всякий случай создаю папку 'data', если она еще не создана
file_path.parent.mkdir(parents=True, exist_ok=True)

try:
    content = ''

    # 1. Сначала проверяю, существует ли файл, и читаю его
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print('Текущее содержимое файла:')
            print(content if content else '[Файл пуст]')
    else:
        print('Файл еще не создан, он будет создан автоматически.')

    # 2. Проверяю, есть ли строка 'Hello world!' в содержимом
    if 'Hello world!' not in content:
        # Если строки нет, открываю файл в режиме дозаписи ('a')
        with open(file_path, 'a', encoding='utf-8') as file:
            # Если файл не пустой и в конце нет переноса строки, добавляю его
            if content and not content.endswith('\n'):
                file.write('\n')

            file.write('Hello world!\n')
        print("Строка 'Hello world!' успешно добавлена в файл.")
    else:
        print("Строка 'Hello world!' уже присутствует в файле, запись не требуется.")

except PermissionError:
    print('Ошибка: Недостаточно прав для чтения или записи этого файла.')
