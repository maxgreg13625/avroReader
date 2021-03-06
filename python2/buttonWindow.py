from PyQt4 import QtGui, QtCore
import commonFunction as cf

class ButtonWindow(QtGui.QWidget):
	def __init__(self, title, avroFileName, buttonType):
		#initialize parent class
		QtGui.QWidget.__init__(self)

		self.setWindowTitle(title)
		self.resize(300,200)
		
		#title is made by imageColumn_rowIndex
		tempList=title.split('_')
		rowIndex=tempList[len(tempList)-1]
		
		recordList=cf.readAvro(avroFileName)
		self.label=QtGui.QLabel()
		
		if buttonType!='Text':
			image=QtGui.QImage()
			image.loadFromData(QtCore.QByteArray.fromBase64(recordList[int(rowIndex)][str(tempList[0])]), buttonType)
			if image.width()>1500 or image.height()>1500:
				image=image.scaled(image.width()/4, image.height()/4)
			self.label.setPixmap(QtGui.QPixmap.fromImage(image))
		else:
			self.label.setText(recordList[int(rowIndex)][str(tempList[0])])

		#add scroll bar for image view
		scroll=QtGui.QScrollArea()
		scroll.setWidget(self.label)
		scroll.setWidgeResizable=True
	
		verticalLayout=QtGui.QVBoxLayout()
		verticalLayout.addWidget(scroll)
		self.setLayout(verticalLayout)

		if buttonType!='Text':
			self.resize(image.width(), image.height())
