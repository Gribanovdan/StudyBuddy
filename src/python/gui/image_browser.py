import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt6.QtGui import QPixmap, QImageReader, QImage, QKeySequence
from PyQt6.QtCore import Qt, QMimeData
import typing as t


class ImageAttachmentWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.images: t.List[QImage]= []
        self.images_path_list: t.List[str] = []

        # Создаем компоненты интерфейса
        self.image_path_line_edit = QLineEdit()
        self.browse_button = QPushButton("Обзор")
        self.preview_label = QLabel()

        # Устанавливаем компоненты в вертикальный макет
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_path_line_edit)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.preview_label)

        # Устанавливаем обработчики событий
        self.browse_button.clicked.connect(self.browse_image)

    def browse_image(self):
        # Открываем диалоговое окно выбора файла
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.gif)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            # Получаем путь к выбранному файлу и устанавливаем его в QLineEdit
            file_path = file_dialog.selectedFiles()[0]
            self.image_path_line_edit.setText(file_path)
            self.preview_image(file_path)

    def preview_image(self, image_path):
        # Отображаем выбранное изображение в QLabel
        pixmap = QPixmap(image_path)
        self.preview_label.setPixmap(pixmap)
        self.preview_label.setScaledContents(True)

    def keyPressEvent(self, event):
        # Проверяем, была ли нажата комбинация клавиш Ctrl+V
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier and event.key() == Qt.Key.Key_V:
            mime_data = QApplication.clipboard().mimeData()

            # Проверяем, содержит ли буфер обмена изображение
            if mime_data.hasImage():
                image = mime_data.imageData()
                image_reader = QImageReader()
                image_reader.read(image)
                image_reader.setAutoTransform(True)

                print('image form clipboard')

                # Сохраняем изображение в файл (или можете использовать в памяти)
                file_path = r"C:\Projects\StudyBuddy\data\pasted_image.png"
                image.save(file_path)

                # Отображаем путь к файлу и превью
                self.image_path_line_edit.setText(file_path)
                self.preview_image(file_path)

            event.accept()
        else:
            super().keyPressEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример прикрепления картинки")

        # Создаем виджет для прикрепления картинки
        self.image_attachment_widget = ImageAttachmentWidget()
        self.setCentralWidget(self.image_attachment_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
