import os

path_1 = 'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\'

new_dir = path_1 + 'temp'


if not os.path.exists(new_dir):
    os.mkdir(new_dir)
