from shutil import copytree
import os, subprocess, datetime, time, signal
from afp_utils import afp_mount

src='/Users/roberthartshorn/Code/Python Projects/BackupSync/Server Backup Staging/Current'
dest='/Users/roberthartshorn/Code/Python Projects/BackupSync/Server Backups/Current'

src_url='"afp://sadmin:BRLa4rxx@fugue/S_B_RAID"'
dest_url='"afp://admin:BRLa4rxx@nas1/NetworkBackups"'

'''TODO: Add a method to verify src/ and dest/ exist.  *Don't forget os.path.isdir' '''

'''TODO:  Add a method to verify that there is a top-level folder in src/ and dest/ for each host in 'expected_backups' '''

'''TODO:  Convert this to use json'''

'''This dictionary maps a host to its volumes.  Only includes volumes that are imaged.'''
expected_backups = {
	'beyonce' :['ServerHD.sparseimage','AppleCore1.sparseimage'],
	'epicor' : ['C','D']
}

print afp_mount(src_url,dest_url)
try:
	copytree(src,dest)
except:
	print "could not copy"
  
'''TODO: consider whether or not we want to use shutil.copystat
          
