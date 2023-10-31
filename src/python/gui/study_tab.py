import typing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

from gui import styles


class StudyTab(QWidget):
    def __init__(self) -> None:
        super().__init__()

        v_layout = QVBoxLayout()

        title_label = QLabel('Ready to study?')
        title_label.setFont(styles.H1)
        title_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        v_layout.addWidget(title_label)

        self.setLayout(v_layout)
