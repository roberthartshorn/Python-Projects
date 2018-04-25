from shutil import copytree
import os, subprocess, datetime, time, signal
from afp_utils import afp_mount
'''These can go away probably as we are parsing the URL for the volume basename
src='/Users/roberthartshorn/Code/Python Projects/StagedBackupTransfer/src/'
dest='/Users/roberthartshorn/Code/Python Projects/StagedBackupTransfer/dest/'
'''

src_url='"afp://sadmin:BRLa4rxx@fugue/S_B_RAID"'
dest_url='"afp://admin:BRLa4rxx@nas1/NetworkBackups"'

'''TODO: Add a method to verify src/ and dest/ exist.  *Don't forget os.path.isdir' '''


'''TODO:  Add a method to verify that there is a top-level folder in src/ and dest/ for each host in 'expected_backups' '''

'''This dictionary maps a host to its volumes.  Only includes volumes that are imaged.'''
'''TODO:  Convert this to use json'''
expected_backups = {
	'beyonce' :['ServerHD.sparseimage','AppleCore1.sparseimage'],
	'epicor' : ['C','D']
}

print afp_mount(src_url,dest_url)


''' try:
          copytree(src,dest)
  except:
          print "There was an unexpected error during copy"
'''