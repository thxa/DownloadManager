# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.uic import loadUiType

from os import path
import sys
import urllib.request

FROM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))


class MainApp(QMainWindow, FROM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui()

    def handle_ui(self):
        self.setWindowTitle("Download manager")
        self.setFixedSize(471, 191)
        self.handle_buttons()

    def handle_buttons(self):
        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.handle_browse)

    def handle_browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files (*.*)")
        name = save_place[0]
        self.lineEdit_2.setText(name)

    def handle_prograse(self, blocknum, blocksize, totalsize):
        read = blocknum * blocksize

        if totalsize > 0:
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents()

    def download(self):
        url = self.lineEdit.text()
        save_local = self.lineEdit_2.text()

        try:
            urllib.request.urlretrieve(url, save_local, self.handle_prograse)
            QMessageBox.information(self, "Download completed", "The Download finshed")
        except Exception:
            QMessageBox.warning(self, "Download Error", "The Download feild")

        self.progressBar.setValue(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")


def main() -> object:
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
