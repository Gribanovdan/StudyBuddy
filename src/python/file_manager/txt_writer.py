import typing as t
import os

from file_manager.dir_manager import get_data_path, ensure_dir

class TxtWriter:
    def __init__(self):
        self._created_files: t.List = []

    def create_workname_file(self, title: str) -> t.Tuple[str, str]:
        '''Returns file path and it's name'''
        file_path = get_data_path('workname.txt')
        ensure_dir(file_path)
        with open(file_path, 'w') as file:
            file.write(title)
        self._created_files.append(file_path)
        return file_path, 'workname.txt'
    
    def create_file(self, name: str, data: str) -> str:
        '''Returns file'''
        file_path = get_data_path(name)
        ensure_dir(file_path)
        with open(file_path, 'w') as file:
            file.write(data)
        self._created_files.append(file_path)
        return file_path

    def delete_all_created_files(self):
        for file_path in self._created_files:
            if os.path.exists(file_path):
                os.remove(file_path)
        self._created_files = []
            