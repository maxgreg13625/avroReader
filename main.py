from PyQt4 import QtGui, QtCore
import ConfigParser
import avroReader as ar
import sys

def readConfig():
	config=ConfigParser.ConfigParser()
	config.read('config.ini')
	imageColumnList=config.get('DEFAULT', 'IMAGE_COLUMN_LIST').split('|')
	imageTypeList=config.get('DEFAULT', 'IMAGE_TYPE_LIST').split('|')

	#make all config as dict
	configDict=dict()
	configDict['IMAGE_COLUMN_LIST']=imageColumnList
	configDict['IMAGE_TYPE_LIST']=imageTypeList
	return configDict

def main():
	configDict=readConfig()

	app=QtGui.QApplication(sys.argv)
	mainWindow=ar.AvroReader(configDict)
	mainWindow.show()
	app.exec_()

if __name__ == '__main__':
	main()
