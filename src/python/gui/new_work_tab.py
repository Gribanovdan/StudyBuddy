import typing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from gui import styles, edit_work_window

from file_manager.zip_writer import ZipWriter
from backend.task_manager import task_manager


class NewWorkTab(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self._allow_creation = False
        self._work_name = False

        v_layout = QVBoxLayout()
        v_layout.setSpacing(30)

        title_label = QLabel('New work upcoming?')
        title_label.setFont(styles.H1)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(title_label)
        v_layout.setAlignment(title_label, Qt.AlignmentFlag.AlignTop)

        work_name_label = QLabel('Enter the name of a new work:')
        work_name_label.setFont(styles.H3)
        work_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(work_name_label)

        self._work_name_line_edit = work_name_line_edit = QLineEdit()
        work_name_line_edit.textChanged.connect(self.on_work_name_changed)
        work_name_line_edit.setFont(styles.ReqularFont)
        work_name_line_edit.setFixedWidth(500)
        work_name_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(work_name_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        work_name_status_label = QLabel('')
        work_name_status_label.setFont(styles.ReqularFont)
        work_name_status_label.setStyleSheet(styles.GreenColor)
        work_name_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.work_name_status_label = work_name_status_label
        v_layout.addWidget(work_name_status_label)

        # Learn to align center
        h_tmp = QHBoxLayout()
        create_button = QPushButton('Create!')
        create_button.setFont(styles.H4)
        create_button.setFixedWidth(350)
        create_button.clicked.connect(self.on_create_button_clicked)
        h_tmp.addStretch(1)
        h_tmp.addWidget(create_button)
        h_tmp.addStretch(1)
        v_layout.addLayout(h_tmp)

        v_layout.addStretch(1)
        self.setLayout(v_layout)

    def show_error(self, msg: str):
        self.work_name_status_label.setStyleSheet(styles.RedColor)
        self.work_name_status_label.setText(msg)

    def on_work_name_changed(self, changed_text):
        if not changed_text:
            self.show_error('Empty input!')
            self._allow_creation = False
        elif task_manager.has_workname(changed_text):
            self.show_error('This work already exists!')
            self._allow_creation = False
        else:
            self.work_name_status_label.setStyleSheet(styles.GreenColor)
            self.work_name_status_label.setText('This name is appropriate, great choice!')
            self._allow_creation = True
            self._work_name = changed_text
            
    def on_create_button_clicked(self):
        if self._allow_creation:
            work_name = self._work_name
            zip_writer = ZipWriter()
            zip_file_path = zip_writer.new_zip(work_name)
            task_manager.add_file(work_name, zip_file_path)
            self._work_name_line_edit.setText('')
            self.edit_window = new_window = edit_work_window.EditWorkWindow(work_name, zip_file_path)
            new_window.show()
            print('expected to be shown')
