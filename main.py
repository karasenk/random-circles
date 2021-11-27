import sys
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            r = randrange(0, 255, 1)
            g = randrange(0, 255, 1)
            b = randrange(0, 255, 1)
            qp.setBrush(QColor(r, g, b))
            side = randrange(1, 300, 1)
            x = randrange(1, 314, 1)
            y = randrange(1, 305, 1)
            qp.drawEllipse(x, y, side, side)
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
