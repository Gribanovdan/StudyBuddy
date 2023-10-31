import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QTabWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QHBoxLayout
)

from gui.study_tab import StudyTab
from gui.new_work_tab import NewWorkTab
from gui import styles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("StudyBuddy")
        self.setFixedSize(700, 400)

        main_container = QWidget()
        layout = QVBoxLayout()

        tabs = QTabWidget()
        tabs.setFont(styles.H4)
        tabs.addTab(StudyTab(), 'Study')
        tabs.addTab(NewWorkTab(), 'New work')

        layout.addWidget(tabs)
        main_container.setLayout(layout)

        self.setCentralWidget(main_container)


def launch_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()