"""
This will create a GUI that the user can interact with.
It will be able to display text and images.
The user can input text into text boxes and the program can use the text.
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

app = QApplication(sys.argv)

app.exec_()