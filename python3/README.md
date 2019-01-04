# avroReader
This is not a general purporse AVRO reader, but with specific situation AVRO viewer. Since some use case will write image binary data into AVRO, it may make AVRO reader spend additional time to display image raw string. This program will display image as a button and show specifc image in a new window.

## configuration
IMAGE_COLUMN_LIST: column store raw image string in AVRO, used '|' to separate each column  
IMAGE_TYPE_LIST: image type for the column above, used '|' to sperate each column  
example:  
IMAGE_COLUMN_LIST=image|corrected|uncorrected  
IMAGE_TYPE_LIST=JPG|PNG|PNG  

## before execution
In order to execute this program, it need to install PyQt5 and fastavro.  
$ sudo pip install pyqt5  
$ sudo pip install Cython  
$ sudo pip install fastavro  

## in order to decompress snappy with snappy format, we need python-snappy instead of snappy
$ sudo pip uninstall snappy
$ sudo pip install python-snappy

## execution
$ python main.py
