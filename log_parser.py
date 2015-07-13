import struct
import binascii

def read(fileNm):

	try:
		fileIn = open(fileNm, 'rb')
	except IOError:
		logging.debug("Could not open input file %s" % (fileNm))
		return
	
	headerBuffer = fileIn.read(128)
	fileIn.seek(fileIn.tell())

	loopBodyBuffer = fileIn.read(320)

	print len(loopBodyBuffer)

    # loop cnt = ( total byte - header byte / stuct size )
	# 1215     = ( 388928 - 128(header byte ) / 320      )

	#i = 0
	#for element int range(0, 1215)
	#print binascii.a2b_hex((loopBodyBuffer[0:4])[0])
	print struct.unpack_from('B', loopBodyBuffer,0)



if __name__ == "__main__":
	read('C:\Users\koo\Desktop\HGL099.LOG') 