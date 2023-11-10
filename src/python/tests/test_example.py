from src.python.file_manager.dir_manager import ensure_dir, get_data_path
import os
import sys

def test_file():
    file_path = get_data_path('test_files/test_file.txt')
    ensure_dir(file_path)
    with open(file_path, 'w') as file:
        file.write('some test text')
    assert os.path.exists(file_path)
