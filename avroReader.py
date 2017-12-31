from PyQt4 import QtGui, QtCore
import commonFunction as cf
import imageWindow as im

class AvroReader(QtGui.QWidget):
	def __init__(self, configDict):
		#initialize parent class
		QtGui.QWidget.__init__(self)

		self.imageColumnList=configDict['IMAGE_COLUMN_LIST']
		self.imageTypeList=configDict['IMAGE_TYPE_LIST']

		self.setWindowTitle('AvroReader Ver 0.1')
		self.resize(300,200)

		fileSelectLayout=QtGui.QHBoxLayout()
		#set for file select text box
		self.fileSelectText=QtGui.QLineEdit()
		self.fileSelectText.readOnly=True
		fileSelectLayout.addWidget(self.fileSelectText)
		#set for file select button
		self.fileSelectButton=QtGui.QPushButton('Select')
		fileSelectLayout.addWidget(self.fileSelectButton)
		#set fro avro read button
		self.avroReadButton=QtGui.QPushButton('Read')
		fileSelectLayout.addWidget(self.avroReadButton)
		#set click event for buttons...
		self.fileSelectButton.clicked.connect(self.selectFile)
		self.avroReadButton.clicked.connect(self.setAvroContent)

		verticalLayout=QtGui.QVBoxLayout()
		verticalLayout.addLayout(fileSelectLayout)
		#set avro schema text
		self.avroSchemaText=QtGui.QTextEdit()
		self.avroSchemaText.readOnly=True
		verticalLayout.addWidget(self.avroSchemaText)
		#set avro record table
		self.avroTable=QtGui.QTableWidget()
		verticalLayout.addWidget(self.avroTable)	
		self.setLayout(verticalLayout)

	def selectFile(self):
		#clear content
		self.fileSelectText.setText('')

		fileName=QtGui.QFileDialog.getOpenFileName(self, 'Open')
		if not fileName.isEmpty():
			self.fileSelectText.setText(fileName)

	def generateImage(self):
		#check which button triger event
		button=self.sender()

		tempList=button.text().split('_')
		self.imageWindow=im.ImageWindow(button.text(), self.fileSelectText.text(), self.imageTypeList[self.imageColumnList.index(tempList[0])])
		self.imageWindow.show()		

	def setAvroContent(self):
		#clear content and table
		self.avroSchemaText.setText('')
		self.avroTable.setColumnCount(0)
		self.avroTable.setRowCount(0)

		recordList, schema=cf.readAvro(self.fileSelectText.text(), withSchema=True)

		#set schema text
		self.avroSchemaText.setText(str(schema))
		
		#set column name
		mainColumns=schema['fields']
		self.avroTable.setColumnCount(len(mainColumns))
		for columnIndex in range(len(mainColumns)):
			self.avroTable.setHorizontalHeaderItem(columnIndex, QtGui.QTableWidgetItem(mainColumns[columnIndex]['name']))

		#set each record
		self.avroTable.setRowCount(len(recordList))
		self.imageButtonDict=dict()
		for rowIndex in range(len(recordList)):
			for columnIndex in range(len(mainColumns)):
				#for the image column, only show button to generate additional window to display image
				if mainColumns[columnIndex]['name'] not in self.imageColumnList:
					self.avroTable.setItem(rowIndex, columnIndex, QtGui.QTableWidgetItem(str(recordList[rowIndex][mainColumns[columnIndex]['name']])))
				else:
					imageIndex='{}_{}'.format(str(mainColumns[columnIndex]['name']), str(rowIndex))
					self.imageButtonDict[imageIndex]=QtGui.QPushButton(imageIndex)
					self.imageButtonDict[imageIndex].clicked.connect(self.generateImage)
					self.avroTable.setCellWidget(rowIndex, columnIndex, self.imageButtonDict[imageIndex])
