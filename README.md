# avroReader
This is not a general purporse AVRO reader, but with specific situation AVRO viewer. Since some use case will write image binary data into AVRO, it may make AVRO reader spend additional time to display image raw string. This program will display image as a button and show specifc image in a new window.

## configuration
IMAGE_COLUMN_LIST: column store raw image string in AVRO, used '|' to separate each column  
IMAGE_TYPE_LIST: image type for the column above, used '|' to sperate each column  
example:  
IMAGE_COLUMN_LIST=image|corrected|uncorrected  
IMAGE_TYPE_LIST=JPG|PNG|PNG  

## before execution
In order to execute this program, it need to install PyQt4 and fastavro.  
$ sudo apt-get install python-qt4  
$ sudo pip install -Iv Cython==0.25.0  #fastavro depends Cython 0.25.0  
$ sudo pip install fastavro  

