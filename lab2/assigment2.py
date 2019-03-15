import os
import sys


os.chroot(os.getcwd())

print("Is it root directory?");
#print("Is it root directory? %s" % os.path.isdir("/"));

#if "/" in os.getcwd():
#	print("Root directory");

#one way of three option to learn is directory root or not
if "root" in os.environ['USERNAME']:
	print(" -Yes root directory");

os.chdir("/");



os.popen('cp -R /bin/ls .');


os.system("whoami");

os.system("ls -la");

