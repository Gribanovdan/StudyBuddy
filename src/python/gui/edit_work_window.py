from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QLabel,
    QComboBox,
    QPushButton,
    QTabWidget,
    QLineEdit,
    QTextEdit
)
from PyQt6.QtGui import QPixmap, QImageReader, QImage, QKeySequence

import typing as t
from gui import styles, image_browser
from common.classes import Task

class EditWorkWindow(QWidget):
    def __init__(self, work_name: str, zip_file: str):
        super().__init__()
        self.max_ind = 0

        self.tasks: t.List[Task] = []
        
        self.setWindowTitle(f'Edit: {work_name}')
        self.setFixedSize(1280, 720)

        layout = QVBoxLayout()

        layout.setSpacing(20)

        title_label = QLabel(f'Edit work \"{work_name}\"')
        title_label.setFont(styles.H1)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        layout.setAlignment(title_label, Qt.AlignmentFlag.AlignTop)


        # ------------HLAYOUT--------------------
        h_layout_top = QHBoxLayout()
        h_layout_top.addStretch(1)

        new_task_button = QPushButton('New task')
        new_task_button.setFont(styles.H4)
        new_task_button.clicked.connect(self.new_task)
        h_layout_top.addWidget(new_task_button)

        delete_task_button = QPushButton('Delete the task')
        delete_task_button.setFont(styles.H4)
        delete_task_button.setStyleSheet(styles.RedColor)
        delete_task_button.clicked.connect(self.delete_task)
        h_layout_top.addWidget(delete_task_button)

        h_layout_top.addStretch(1)
        layout.addLayout(h_layout_top)
        # ----------------------------------------

        self.task_tabs = task_tabs = QTabWidget()
        task_tabs.setFont(styles.RegularFont)
        task = Task(ind=0, title='test title')
        task_tabs.addTab(TaskWidget(task_tabs, task), 'Test')

        layout.addWidget(task_tabs)

        layout.addStretch(1)
        self.setLayout(layout)

    def new_task(self):
        new_task = Task(self.max_ind)
        self.max_ind += 1
        self.task_tabs.addTab(TaskWidget(self.task_tabs, new_task), 'New task')

    def delete_task(self):
        self.task_tabs.currentWidget().deleteLater()


class TaskWidget(QWidget):
    def __init__(self, my_tab: QTabWidget, task: Task):
        super().__init__()
        two_columns = QHBoxLayout()
        self.my_tab = my_tab
        self.my_task = task
        
        self.left = left_layout = QVBoxLayout()
        self.right = right_layout = QVBoxLayout()
        two_columns.addLayout(left_layout)
        two_columns.addLayout(right_layout)
        
        self.setup_left_column()
        self.setup_right_column()

        self.setLayout(two_columns)
        
    def setup_left_column(self):
        clear_layout(self.left)
        title = QLabel('Title of the task')
        title.setFont(styles.H4)
        title_line_edit = QLineEdit()
        title_line_edit.textChanged.connect(self.on_title_changed)
        self.left.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.left.addWidget(title_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)

        question_label = QLabel('Question')
        question_label.setFont(styles.H4)
        self.left.addWidget(question_label, alignment=Qt.AlignmentFlag.AlignCenter)
        question_text_edit = QTextEdit()
        self.left.addWidget(question_text_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        question_button = QPushButton('Add Images')
        question_button.clicked.connect(self.on_question_clicked)
        self.left.addWidget(question_button, alignment=Qt.AlignmentFlag.AlignCenter)

        tip_label = QLabel('Tip')
        tip_label.setFont(styles.H4)
        self.left.addWidget(tip_label, alignment=Qt.AlignmentFlag.AlignCenter)
        tip_line_edit = QLineEdit()
        self.left.addWidget(tip_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        tip_button = QPushButton('Add Images')
        tip_button.clicked.connect(self.on_tip_clicked)
        self.left.addWidget(tip_button, alignment=Qt.AlignmentFlag.AlignCenter)

        answer_label = QLabel('Answer')
        answer_label.setFont(styles.H4)
        self.left.addWidget(answer_label, alignment=Qt.AlignmentFlag.AlignCenter)
        answer_text_edit = QTextEdit()
        self.left.addWidget(answer_text_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        answer_button = QPushButton('Add Images')
        answer_button.clicked.connect(self.on_answer_clicked)
        self.left.addWidget(answer_button, alignment=Qt.AlignmentFlag.AlignCenter)

        comment_label = QLabel('Comment')
        comment_label.setFont(styles.H4)
        self.left.addWidget(comment_label, alignment=Qt.AlignmentFlag.AlignCenter)
        comment_line_edit = QLineEdit()
        self.left.addWidget(comment_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        comment_button = QPushButton('Add Images')
        comment_button.clicked.connect(self.on_comment_clicked)
        self.left.addWidget(comment_button, alignment=Qt.AlignmentFlag.AlignCenter)
    
    def setup_right_column(self):
        clear_layout(self.right)
        title = QLabel('Right column')
        self.right.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

    def on_title_changed(self, new_title: str):
        cur_tab_ind = self.my_tab.currentIndex()
        self.my_tab.setTabText(cur_tab_ind, new_title)

    def on_question_clicked(self):
        self.open_image_browser([])

    def on_tip_clicked(self):
        self.open_image_browser([])

    def on_answer_clicked(self):
        self.open_image_browser([])

    def on_comment_clicked(self):
        self.open_image_browser([])

    def open_image_browser(self, images_list: t.List[QImage]):
        self.select_window = image_browser.ImageAttachmentWidget()
        self.select_window.show()

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()