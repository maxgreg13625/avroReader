import fastavro as avro

def readAvro(fileName, withSchema=False):
	schema=None
	recordList=None

	if not fileName=='':
		with open(fileName, 'rb') as fd:
			reader=avro.reader(fd)
			schema=reader.schema
			recordList=list(reader)

	if withSchema:
		return recordList, schema
	else:
		return recordList

def getAvroRecord(fileName, row, column):
	recordList=readAvro(fileName)

	return recordList[int(row)][column]
