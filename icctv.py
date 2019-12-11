#yoman

from id  import *
import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"

def main():
	os.system('clear')
	print ("{}CCTV GOKIL ID").format(g)
	print ("")
	print ("Pilih : ")
	print ("(1) {}cctv Indonesia").format(g)
	print ("(2) Keluar")
	print ""
	select = input("pilih wey -> ")
	filtering(select)

def filtering(pilih):
	if pilih == 1:
	   indonesia()
	elif pilih == 2:
	   print ("Keluarrr...")
	   os.sys.exit()

if __name__ == '__main__':
	main()

