import os
from typing import Iterable, Tuple


def walk(top: str) -> Iterable[Tuple]:
  files_and_folders = os.listdir(path=top)
  c_folders = [elem for elem in files_and_folders if not '.' in elem] 
  c_files = [elem for elem in files_and_folders if '.' in elem] 

  yield (top, c_folders, c_files) #walk сообщает информацию о текущей директории top

  for c_folder in c_folders: #проход по всем папкам с вызовом walk
    for root, folders, files in walk(top=top+'/'+c_folder):
      yield (root, folders, files)
    


for root, folders, files in walk("/home/neo"): #вывод не только корневых папок, но и самой директории
    # Doing something, for example:
    print(f"Folder \"{root}\" contains {len(folders)} folders and {len(files)} files.")
