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

print('System time:', time_now)  # POSIX время - float секунды с 01-01-1970
print('File created:', created_time)
print(f'File modified {round((updated_time - created_time) / 60)} minutes ago')
print(f'Time of last file usage {access_time}')
