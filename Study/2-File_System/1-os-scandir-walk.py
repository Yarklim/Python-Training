import os

# Набор команд для модуля os находится в файле usefull_os-funcs.py

path_1 = (
    'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data'
)

path_2 = 'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System'

exlude_dirs = ['root', 'temp', 'etc']  # директории, которые надо исключить из поиска

# ---------------- scandir - просматривает переданную директорию ----------------
for i in os.scandir(path_1):
    print(i)  # <DirEntry 'key.txt'>
    print(
        i.path, i.is_dir(), i.is_file()
    )  # C:\Users\Yarklim\Desktop\Python\Python-Training\Study\2-File_System\data\key.txt False True

# ---------------- walk - просматривает всю глубину переданной директории ----------------
for i in os.walk(path_2):
    print(i)
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System', ['data', 'etc'], ['1-os-candir_os_walk.py'])
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data', [], ['key.txt', 'one.txt'])
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\etc', [], ['test.txt'])

paths = []

for address, dirs, files in os.walk(path_2):
    for exlude in exlude_dirs:
        if exlude in dirs:
            dirs.remove(exlude)  # исключаю директорию из поиска если надо

    for file in files:
        if '.txt' in file:
            paths.append(os.path.join(address, file))

print(
    paths
)  # ['C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data\\key.txt', 'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data\\one.txt']
