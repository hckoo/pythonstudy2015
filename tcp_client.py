import socket
import thread

def recv_thread(args):
	clientsocket = args

	while 1:		
		try:
			msg = clientsocket.recv(4096)
			print "recv : %s" % msg


		except socket.error:
			print "server disconnect"
			break
	
	clientsocket.close()

if "__main__" == __name__:
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect(('127.0.0.1', 5000))

	thread.start_new_thread(recv_thread, (clientsocket,))

	while True:
		msg = raw_input()
		if "exit" == msg:
			break

		clientsocket.send(msg)

	clientsocket.close()