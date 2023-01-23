################################################################################
##
## BY:      Sunil Patel
## MODULE:  Splash screen whilst loading the application
##
################################################################################

import sys

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QEvent,
                          QMetaObject, QObject, QPoint, QPropertyAnimation,
                          QRect, QSize, Qt, QTime, QUrl)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                         QPainter, QPalette, QPixmap, QRadialGradient)
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
                             QDateTimeEdit, QDial, QDoubleSpinBox,
                             QFontComboBox, QGraphicsDropShadowEffect, QLabel,
                             QLCDNumber, QLineEdit, QMainWindow, QProgressBar,
                             QPushButton, QRadioButton, QSlider, QSpinBox,
                             QTimeEdit, QVBoxLayout, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        ## UI ==> INTERFACE
        ########################################################################
        uic.loadUi("main.ui", self)
        self.label = self.findChild(QLabel, "label")

        # MAIN WINDOW LABEL ON CLOSING DOWN (AFTER TIMER)
        QtCore.QTimer.singleShot(2500, lambda: self.label.setText("<strong>THANKS</strong> FOR WATCHING"))
        QtCore.QTimer.singleShot(2500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))



class SplashScreen(QMainWindow):    
    def __init__(self):
        super().__init__()

        ## UI ==> INTERFACE
        ########################################################################
        uic.loadUi("splash_screen.ui", self)
        self.progress_bar = self.findChild(QProgressBar, "progressBar")
        self.label_stage = self.findChild(QLabel, "label_stage")

        ## UI ==> SETTINGS
        ########################################################################

        ## REMOVE SPLASH SCREEN TITLE BAR
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## SPLASH SCREEN QTIMER PROGRESS BAR
        self.counter = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)

        # SPLASH SCREEN TEXT
        # TODO Replace with build steps
        self.label_stage.setText("WELCOME TO <strong>DAISYCATTAX</strong>")
        self.timer.singleShot(800, lambda: self.label_stage.setText("LOADING <strong>DATABASE</strong>"))
        self.timer.singleShot(1200, lambda: self.label_stage.setText("MATCHING <strong>TRANSACTIONS</strong>"))
        self.timer.singleShot(1500, lambda: self.label_stage.setText("LOADING <strong>USER INTERFACE</strong>"))

        self.show()

    ## ==> CLASS METHODS
    ########################################################################
    def progress(self):
        self.progress_bar.setValue(self.counter)
        self.counter += 1
        
        if self.counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()    
    sys.exit(app.exec())
