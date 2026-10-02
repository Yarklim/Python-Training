import os

path_1 = (
    'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data'
)

path_2 = 'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System'

# ---------------- scandir - просматривает файлы и папки в переданной директории ----------------
for i in os.scandir(path_1):
    print(i)  # <DirEntry 'key.txt'>
    print(
        i.path, i.is_dir(), i.is_file()
    )  # C:\Users\Yarklim\Desktop\Python\Python-Training\Study\2-File_System\data\key.txt False True

# ---------------- walk - просматривает всю глубину переданной директории ----------------
for i in os.walk(path_2):
    print(i)
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System', ['data'], ['1-os-candir_os_walk.py'])
# ('C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data', [], ['key.txt', 'one.txt'])
