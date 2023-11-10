import zipfile
import os

from file_manager.dir_manager import ensure_dir, get_data_path
from file_manager.txt_writer import TxtWriter
from common.classes import Task

class ZipWriter:
    _max_ind = 0
    
    def __init__(self) -> None:
        self._txt_writer = TxtWriter()
        self._task_zips = []

    def new_zip(self, work_name: str) -> str:
        file_name = str(ZipWriter._max_ind) + '.zip'
        self._zip_file_path = get_data_path(file_name)
        ensure_dir(self._zip_file_path)
        zipf = self._cur_opened_zip = zipfile.ZipFile(self._zip_file_path, 'w')
        ZipWriter._max_ind += 1
        workname_file_path, workname_file_name = self._txt_writer.create_workname_file(work_name)
        zipf.write(workname_file_path, workname_file_name)
        self._txt_writer.delete_all_created_files()
        return self._zip_file_path
        
    def new_task(self, task: Task):
        file_name = 'task' + str(task.ind) + '.zip'
        zip_path = get_data_path(file_name)
        ensure_dir(zip_path)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            if task.question:
                f = self._txt_writer.create_file('question.txt', task.question)
                zipf.write(f, 'question.txt')
            if task.question_images:
                pass
            if task.tip:
                f = self._txt_writer.create_file('tip.txt', task.tip)
                zipf.write(f, 'tip.txt')
            if task.tip_images:
                pass
            if task.answer:
                f = self._txt_writer.create_file('answer.txt', task.answer)
                zipf.write(f, 'answer.txt')
            if task.answer_images:
                pass
            if task.comment:
                f = self._txt_writer.create_file('comment.txt', task.comment)
                zipf.write(f, 'comment.txt')
            if task.comment_images:
                pass
            self._txt_writer.delete_all_created_files()
        self._cur_opened_zip.write(zip_path, file_name)
        os.remove(zip_path)
