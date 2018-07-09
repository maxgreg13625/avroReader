from PyQt5 import QtGui, QtWidgets, QtCore
from time import gmtime, strftime
import base64
import commonFunction as cf

class ButtonWindow(QtWidgets.QWidget):
	def __init__(self, title, avroFileName, buttonType):
		#initialize parent class
		QtWidgets.QWidget.__init__(self)

		self.setWindowTitle(title)
		self.resize(300,200)

		#title is made by imageColumn_rowIndex
		tempList=title.split('_')
		rowIndex=tempList[len(tempList)-1]

		#set generate image file button
		self.generateImgFileButton=QtWidgets.QPushButton('To File')
		self.generateImgFileButton.clicked.connect(lambda: self.generateImgFile(buttonType))

		self.content=cf.getAvroRecord(avroFileName, rowIndex, tempList[0])
		self.label=QtWidgets.QLabel()
		
		if buttonType!='Text':
			image=QtGui.QImage()
			image.loadFromData(QtCore.QByteArray.fromBase64(self.content.encode()), buttonType)
			if image.width()>1500 or image.height()>1500:
				image=image.scaled(image.width()/4, image.height()/4)
			self.label.setPixmap(QtGui.QPixmap.fromImage(image))
		else:
			self.label.setText(self.content)

		#add scroll bar for image view
		scroll=QtWidgets.QScrollArea()
		scroll.setWidget(self.label)
		scroll.setWidgeResizable=True
	
		verticalLayout=QtWidgets.QVBoxLayout()
		verticalLayout.addWidget(self.generateImgFileButton)
		verticalLayout.addWidget(scroll)
		self.setLayout(verticalLayout)

		if buttonType!='Text':
			self.resize(image.width(), image.height())

	def generateImgFile(self, buttonType):
		imgName=strftime('%Y%m%d%H%M%S', gmtime())

		with open('{}.{}'.format(imgName, buttonType), 'wb') as f:
			if buttonType!='Text':
				f.write(base64.b64decode(self.content))
			else:
				f.write(self.content)
