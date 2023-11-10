from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel
)

from gui import styles
from common.classes import Task

class EditWorkWindow(QWidget):
    def __init__(self, work_name: str, zip_file: str):
        super().__init__()
        
        self.setWindowTitle(f'Edit: {work_name}')
        self.setFixedSize(1280, 720)

        layout = QVBoxLayout()

        layout.setSpacing(30)

        title_label = QLabel(f'Edit work \"{work_name}\"')
        title_label.setFont(styles.H1)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        layout.setAlignment(title_label, Qt.AlignmentFlag.AlignTop)
        layout.addStretch(1)
        self.setLayout(layout)


class TaskWidget(QWidget):
    def __init__(self, Task):
        layout = QVBoxLayout()

        layout.setSpacing(30)

        title_label = QLabel(f'Edit work \"{work_name}\"')
        title_label.setFont(styles.H1)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        layout.setAlignment(title_label, Qt.AlignmentFlag.AlignTop)
        
        two_columns = QHBoxLayout()
        layout.addWidget(two_columns)
        
        self.left = left_layout = QVBoxLayout()
        self.right = right_layout = QVBoxLayout()
        two_columns.addWidget(left_layout)
        two_columns.addWidget(right_layout)
        
        self.setup_left_column(left_layout)
        self.setup_right_column(right_layout)
        
        layout.addStretch(1)

        self.setLayout(layout)
        
    def setup_left_column(self, layout):
        title = QLabel('Fields')
    
    def setup_right_column(self, layout):
        pass
