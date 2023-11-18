import sys

from PyQt5.QtWidgets import QApplication

from clases.MainWindow import MyLib

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_lib = MyLib()
    my_lib.show()
    sys.exit(app.exec_())
