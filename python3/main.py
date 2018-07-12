from PyQt5 import QtWidgets 
import configparser
import avroReader as ar
import sys

def readConfig():
	config=configparser.ConfigParser()
	config.read('./config.ini')
	imageColumnList=config.get('DEFAULT', 'BUTTON_COLUMN_LIST').split('|')
	imageTypeList=config.get('DEFAULT', 'BUTTON_TYPE_LIST').split('|')

	#make all config as dict
	configDict=dict()
	configDict['BUTTON_COLUMN_LIST']=imageColumnList
	configDict['BUTTON_TYPE_LIST']=imageTypeList
	return configDict

def main():
	configDict=readConfig()

	app=QtWidgets.QApplication(sys.argv)
	mainWindow=ar.AvroReader(configDict)
	mainWindow.show()
	app.exec_()

if __name__ == '__main__':
	main()
