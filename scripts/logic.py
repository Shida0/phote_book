from log import *
from sign_in import *
from welcome import *
from PyQt5 import *

class logic(QtWidgets.QMainWindow):
	def __init__(self):
		super(logic, self).__init__()

		self.ui_log = Ui_MainWindow_log()
		self.ui_sign_in = Ui_MainWindow_sign_in()
		self.ui_welcome = Ui_MainWindow_welcome()

		self.ui_log.setupUi(self)
		self.ui_welcome.setupUi(self)
		self.ui_sign_in.setupUi(self)
