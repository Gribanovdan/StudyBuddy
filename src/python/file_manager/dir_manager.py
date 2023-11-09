import os


def ensure_dir(file_full_path):
    directory = os.path.dirname(file_full_path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_data_path(file_name: str):
    return os.path.join(os.getcwd(), 'data', file_name)