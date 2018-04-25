from shutil import copytree
import os, subprocess, datetime, time, signal
from afp_utils import afp_mount

def main():
	src='/Users/roberthartshorn/Code/Python Projects/BackupSync/Server Backup Staging/Current'
	dest='/Users/roberthartshorn/Code/Python Projects/BackupSync/Server Backups/Current'

	src_afp_url='"afp://sadmin:BRLa4rxx@fugue/S_B_RAID"'
	dest_afp_url='"afp://admin:BRLa4rxx@nas1/NetworkBackups"'

	'''This dictionary maps a host to a list of expected backup volumes.'''
	'''TODO:  Consider converting this to use json'''
	expected_backups = {
		'beyonce' :['ServerHD.sparseimage','AppleCore1.sparseimage'],
		'epicor' : ['C','D']
	}

	print afp_mount(src_afp_url,dest_afp_url)
	try:
		'''TODO: consider whether or not we want to use shutil.copystat'''
		copytree(src,dest)
	except Exception as e:
		print e

if __name__ == '__main__':
	print main()



  

          
