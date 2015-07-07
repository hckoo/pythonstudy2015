import os
import os.path
import sys
import ConfigParser
import win32wnet

def netcopy(host, source, dest_dir, username=None, password=None, move=False):
    """ Copies files or directories to a remote computer. """
    
    wnet_connect(host, username, password)
            
    dest_dir = covert_unc(host, dest_dir)

    # Pad a backslash to the destination directory if not provided.
    if not dest_dir[len(dest_dir) - 1] == '\\':
        dest_dir = ''.join([dest_dir, '\\'])

    # Create the destination dir if its not there.
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    else:
        # Create a directory anyway if file exists so as to raise an error.
         if not os.path.isdir(dest_dir):
             os.makedirs(dest_dir)

    # if move:
    #     shutil.move(source, dest_dir)
    # else:
    #     shutil.copy(source, dest_dir)


def covert_unc(host, path):
    """ Convert a file path on a host to a UNC path."""
    return ''.join(['\\\\', host, '\\', path.replace(':', '$')])
    
def wnet_connect(host, username, password):
    unc = ''.join(['\\\\', host])
    try:
        win32wnet.WNetAddConnection2(0, None, unc, None, username, password)
    except Exception, err:
        if isinstance(err, win32wnet.error):
            # Disconnect previous connections if detected, and reconnect.
            if err[0] == 1219:
                win32wnet.WNetCancelConnection2(unc, 0, 0)
                return wnet_connect(host, username, password)
        raise err


def ini_read():
	# ip, id , pass
	config = ConfigParser.ConfigParser()
	config.read("test.ini")

	IPs = config.get('TOBE_INTERFACE','IP').split(',')
	IDs = config.get('TOBE_INTERFACE','ID').split(',')
	PWs = config.get('TOBE_INTERFACE','PW').split(',')

	for i in range(len(IPs)):
		print IPs[i]
		print IDs[i]
		print PWs[i]



def main():
    # if not len(sys.argv) >= 3:
    #     print "copy src [src2 src3..] dst"
    #     return

    # for src in sys.argv[1:-1]:
    #     copy(src, sys.argv[-1], threadcopy)
    print 'aaa'

if __name__ == '__main__':
    # main()
	ini_read()