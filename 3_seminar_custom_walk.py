import os
from typing import List, Tuple

def walk(top: str) -> List[Tuple]: #информация не только о корневых, но и о основной вызванной директории
    tuples_rff = []

    files_and_folders = os.listdir(path=top)
    c_folders = [elem for elem in files_and_folders if not '.' in elem] 
    c_files = [elem for elem in files_and_folders if '.' in elem] 

    tuples_rff.append((top, c_folders, c_files)) #передаем информацию о текущей директории top

    for c_folder in c_folders: #проход по всем папкам с забором информации о них
        for root, folders, files in walk(top=top+'/'+c_folder):
            tuples_rff.append((root, folders, files))
    return tuples_rff
