# 1. В корне проекта создать виртуальное окружение
py -m venv .venv

# 2. Активировать venv в Bash / Git Bash
source .venv/Scripts/activate

# 3. Проверить, что venv активен
python --version
python -m pip --version
which python

# Ожидаемый путь:
.../.venv/Scripts/python

# 4. Обновить pip внутри venv
python -m pip install --upgrade pip

# 5. Проверить, что python.exe внутри .venv существует
ls .venv/Scripts/python.exe

# 6. Выбрать интерпретатор в VSCode:
Ctrl + Shift + P
→ Python: Select Interpreter
→ выбрать .venv/Scripts/python.exe

Если его нет в списке:
→ Enter interpreter path...
→ Find...
→ выбрать: <путь_к_проекту>/.venv/Scripts/python.exe

# 7. Устанавливать пакеты только через активированный venv
python -m pip install package-name

# 8. Сохранить зависимости:
python -m pip freeze > requirements.txt