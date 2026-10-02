import os

path = (
    'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\data'
)

for i in os.scandir(path):
    print(i)  # <DirEntry 'key.txt'>
    print(
        i.path, i.is_dir(), i.is_file()
    )  # C:\Users\Yarklim\Desktop\Python\Python-Training\Study\2-File_System\data\key.txt False True
