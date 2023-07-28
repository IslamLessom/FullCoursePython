import os
import shutil

path = "folder"

try:
    #os.remove(path) #удаление файлов
    #os.rmdir(path) #удаление папок
    if not os.path.exists(path):
        os.makedirs(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("That files was not found")
except PermissionError:
    print('You do not have permission ti delete that')
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
