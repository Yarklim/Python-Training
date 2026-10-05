import os
import time  # операционное время

dir_path = (
    'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\'
)
file_path = dir_path + '3-walk-time.py'

time_now = time.time()
created_time = os.path.getctime(
    file_path
)  # на Windows - время создания, Mac/Linux - время изменения метаданных файла
updated_time = os.path.getmtime(file_path)  # время изменения файла
access_time = os.path.getatime(file_path)  # время последнего использования файла

# print('System time:', time_now)  # POSIX время - float секунды с 01-01-1970
# print('File created:', created_time)
# print(f'File modified {round((updated_time - created_time) / 60)} minutes ago')
# print(f'Time of last file usage {access_time}')

# ------------------ Поиск по дате создания -------------------
query = input('What search?\n')
time_stamp = int(input('Enter how many hours ago the file was created.\n') or 0) * 3600

matches = []

for address, dirs, files in os.walk(dir_path):
    for file in files:
        if query in file:
            full_path = os.path.join(address, file)

            if os.path.islink(
                full_path
            ):  # проверка на битую символическую ссылку файла
                continue

            if time_stamp:
                if time_now - os.path.getctime(full_path) < time_stamp:
                    matches.append(full_path)
            else:
                matches.append(full_path)

print(matches)
