import socket
import thread

def loopback_thread(clientsocket, addr):
	print "Run loopback thread!"
	while 1:		
		try:
			msg = clientsocket.recv(4096)
			print "[%s, recv] : %s" % (addr, msg)
			clientsocket.send(msg)


		except socket.error:			
			break;

	print "Close %s section" % str(addr)
	clientsocket.close()


if "__main__" == __name__:
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('127.0.0.1', 5000))
	serversocket.listen(5)

	while True:
		print "wait..."
		(clientsocket, address) = serversocket.accept()
		print "client(%s) connection ok!" % str(address)
		thread.start_new_thread(loopback_thread, (clientsocket, address))

	serversocket.close()