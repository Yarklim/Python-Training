import os
import time  # операционное время

dir_path = (
    'C:\\Users\\Yarklim\\Desktop\\Python\\Python-Training\\Study\\2-File_System\\'
)
file_path = dir_path + '3-walk-time.py'

change_time = os.path.getctime(
    file_path
)  # на Windows - время создания, Mac/Linux - время изменения

print('System time:', time.time())  # POSIX время - float секунды с 01-01-1970
print('File created:', change_time)
