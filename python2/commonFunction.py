import fastavro as avro

def readAvro(fileName, withSchema=False):
	schema=None
	recordList=None

	if not fileName.isEmpty():
		with open(fileName, 'rb') as fd:
			reader=avro.reader(fd)
			schema=reader.schema
			recordList=list(reader)

	if withSchema:
		return recordList, schema
	else:
		return recordList
