from PyQt4 import QtGui, QtCore
import commonFunction as cf

class ImageWindow(QtGui.QWidget):
	def __init__(self, title, avroFileName, imgType):
		#initialize parent class
		QtGui.QWidget.__init__(self)

		self.setWindowTitle(title)
		self.resize(300,200)

		#title is made by imageColumn_rowIndex
		tempList=title.split('_')
		rowIndex=tempList[len(tempList)-1]

		recordList=cf.readAvro(avroFileName)
		self.imageLabel=QtGui.QLabel()
		image=QtGui.QImage()
		#assume all image are JPG type
		image.loadFromData(QtCore.QByteArray.fromBase64(recordList[int(rowIndex)][str(tempList[0])]), imgType)
		self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

		#add scroll bar for image view
		scroll=QtGui.QScrollArea()
		scroll.setWidget(self.imageLabel)
		scroll.setWidgeResizable=True

		verticalLayout=QtGui.QVBoxLayout()
		verticalLayout.addWidget(scroll)
		self.setLayout(verticalLayout)
		self.resize(image.width(), image.height())
