import sys
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QLabel, QScrollBar, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtGui import QPixmap, QColor, QIcon,QImage, QPainter, QPen


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__(None)
        
        self.setWindowTitle('GOL Engine')
       
        self.central_layout = QVBoxLayout()
        self.central_label = QLabel()
        self.central_layout.addWidget(central_label)
        image = QImage(200, 200, QImage.Format_RGB32)
        painter = QPainter(image)
        # painter.setBrush()
        pen = QPen(Qt.red)
        pen.setWidth(5)
        painter.setPen(pen)
        painter.drawRect(50, 50, 200, 200)
        painter.end()
        central_label.setPixmap(QPixmap.fromImage(image) )
   
    
    



def main():
    app = QApplication(sys.argv)
    w = MyApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()