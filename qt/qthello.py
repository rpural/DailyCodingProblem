#! /usr/bin/env python3

''' Simple Hello World example using PyQt5 '''

import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

# Create the application's GUI
window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)

helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

# Display the window
window.show()

# Enter the run loop
sys.exit(app.exec_())
