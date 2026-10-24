import os

# Набор команд для модуля os находится в файле usefull_os-funcs.py

path_1 = (
    'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data'
)

path_2 = 'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System'

exclude_dirs = ['root', 'temp', 'etc']  # директории, которые надо исключить из поиска

# ---------------- scandir - просматривает переданную директорию ----------------
for entry in os.scandir(path_1):
    print(entry)  # <DirEntry 'key.txt'>
    print(
        entry.path, entry.is_dir(), entry.is_file()
    )  # C:\Users\Yarklim\Desktop\Python\Python-Training\Study\2-File_System\data\key.txt False True

# ---------------- walk - просматривает всю глубину переданной директории ----------------
for root, dirs, files in os.walk(path_2):
    print(root, dirs, files)
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System', ['data', 'etc'], ['1-os-candir_os_walk.py'])
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data', [], ['key.txt', 'one.txt'])
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\etc', [], ['test.txt'])

paths = []

for address, dirs, files in os.walk(path_2):
    # Безопасно удаляю папки из списка прямо во время обхода
    dirs[:] = [d for d in dirs if d not in exclude_dirs]

    for file in files:
        if file.endswith('.txt'):  # Идиоматичный способ проверки расширения
            paths.append(os.path.join(address, file))

print(
    paths
)  # ['C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data\\key.txt', 'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data\\one.txt']
