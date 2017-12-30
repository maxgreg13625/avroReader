from PyQt4 import QtGui, QtCore
import ConfigParser
import avroReader as ar
import sys

def readConfig():
	config=ConfigParser.ConfigParser()
	config.read('config.ini')
	imageColumnList=config.get('DEFAULT', 'IMAGE_COLUMN_LIST').split('|')

	return imageColumnList

def main():
	imageColumnList=readConfig()

	app=QtGui.QApplication(sys.argv)
	mainWindow=ar.AvroReader(imageColumnList)
	mainWindow.show()
	app.exec_()

if __name__ == '__main__':
	main()
