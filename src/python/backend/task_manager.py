import typing as t

class TaskManager:
    def __init__(self) -> None:
        self._work_name_file_map: t.Dict[str, str] = {}
        self._file_work_name_map: t.Dict[str, str] = {}
        
    def has_workname(self, workname: str) -> bool:
        return workname in self._work_name_file_map

    def add_file(self, work_name: str, file_name: str):
        self._work_name_file_map[work_name] = file_name
        self._file_work_name_map[file_name] = work_name


task_manager = TaskManager()
