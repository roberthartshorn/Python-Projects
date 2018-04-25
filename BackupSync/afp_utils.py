import os 

def afp_mount(src_url,dest_url):
	'''A method to mount afp volumes'''
	src_mountpoint='/Volumes/' + os.path.basename(src_url).replace('"','')
	dest_mountpoint='/Volumes/' + os.path.basename(dest_url).replace('"','')

	print src_mountpoint

	targets = {
		'src': {
			'isMounted': True if os.path.exists(src_mountpoint) else False, 
			'url': src_url
		}, 
		'dest': {
			'isMounted': True if os.path.exists(dest_mountpoint) else False, 
			'url': dest_url
		}
	}

	for key, value in targets.iteritems():
		if targets[key]['isMounted'] is False:
			print 'Will attempt to mount volume ' + key +  ' at: ' + targets[key]['url']
		else:
			print 'Volume ' + key + ' is already mounted'


	#mount_string = '\'mount volume \"afp://sadmin:BRLa4rxx@fugue/S_B_RAID\"\''
	#print mount_string

	'''TODO: def unmount():'''

''' This method was written by Rui Carmo and thosascript -e 'mount volume "afp://sadmin:BRLa4rxx@fugue/S_B_RAID"e source is found here:  https://taoofmac.com/space/blog/2010/10/23/2216'''
def waitfor(command, timeout):
    """call shell-command and either return its output or kill it
    if it doesn't normally exit within timeout seconds and return None"""
    start = datetime.datetime.now()
    '''TODO:  Implement stderr=p.communicate() instead as that is best practice for getting an stderr pipe'''
    process = subprocess.Popen(command, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while process.poll() is None:
        time.sleep(0.2)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return None
    return process.stdout.readlines()