import typing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from gui import styles



class NewWorkTab(QWidget):
    def __init__(self) -> None:
        super().__init__()

        v_layout = QVBoxLayout()
        v_layout.setSpacing(30)

        title_label = QLabel('New work upcoming?')
        title_label.setFont(styles.H1)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(title_label)
        v_layout.setAlignment(title_label, Qt.AlignmentFlag.AlignTop)

        work_name_label = QLabel('Enter name of new work:')
        work_name_label.setFont(styles.H3)
        work_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(work_name_label)

        work_name_line_edit = QLineEdit()
        work_name_line_edit.textChanged.connect(self.on_work_name_changed)
        work_name_line_edit.setFont(styles.ReqularFont)
        work_name_line_edit.setFixedWidth(500)
        work_name_line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(work_name_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        work_name_status_label = QLabel('OK')
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
        h_tmp.addStretch(1)
        h_tmp.addWidget(create_button)
        h_tmp.addStretch(1)
        v_layout.addLayout(h_tmp)

        v_layout.addStretch(1)
        self.setLayout(v_layout)


    def on_work_name_changed(self, changed_text):
        def show_error(msg: str):
            self.work_name_status_label.setStyleSheet(styles.RedColor)
            self.work_name_status_label.setText(msg)
        if not changed_text:
            show_error('Empty input!')
        elif 'Куцко' in changed_text:
            show_error('Loser!')
        else:
            self.work_name_status_label.setStyleSheet(styles.GreenColor)
            self.work_name_status_label.setText('This name is appropriate, great choice!')