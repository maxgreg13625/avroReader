#http://ftp.ics.uci.edu/pub/centos0/ics-custom-build/BUILD/PyQt-x11-gpl-4.7.2/examples/widgets/imageviewer.py
#follow above link to modify...
from PyQt4 import QtGui, QtCore
import commonFunction as cf

class ImageWindow(QtGui.QWidget):
	def __init__(self, title, avroFileName):
		#initialize parent class
		QtGui.QWidget.__init__(self)

		self.setWindowTitle(title)
		self.resize(300,200)
		tempList=title.split('_')
		rowIndex=tempList[len(tempList)-1]
		
		recordList=cf.readAvro(avroFileName)
		self.imageLabel=QtGui.QLabel()
		image=QtGui.QImage()
		image.loadFromData(QtCore.QByteArray.fromBase64(str(recordList[int(rowIndex)]['image'])), 'JPG')
		self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

		verticalLayout=QtGui.QVBoxLayout()
		verticalLayout.addWidget(self.imageLabel)
		self.setLayout(verticalLayout)
		self.resize(image.width(), image.height())
