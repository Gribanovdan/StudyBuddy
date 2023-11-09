import typing as t

from src.python.common import errors

class Processor:
    def __init__(self) -> None:
        self._work_name_file_map: t.Dict[str, str] = {}
        self._file_work_name_map: t.Dict[str, str] = {}

    def add_file(self, work_name: str, file_name: str):
        if work_name in self._work_name_file_map:
            raise errors.ProcessorError(f'Work with name {work_name} already exists in processor!')
        self._work_name_file_map[work_name] = file_name
        self._file_work_name_map[file_name] = work_name