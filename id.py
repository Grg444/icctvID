#yoman

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


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; RMX1971) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'}


def indonesia():
	global page
	res = requests.get('https://www.insecam.org/en/bycountry/ID/', headers=headers)
	findpage = re.findall('"?page=",\s\d+', res.text)[1]
	grg = findpage.replace('page=",', '')
	os.system('clear')
	print ('{}----------').format(g)
	print ('{}CCTV GOKIL').format(w)
	print ('{}----------').format(g)
	print ('{}	( {}jumlah halaman{} : {} {} )').format(g,y,r,grg,g)
	run()

def run():
     try:
	print ("")
	page = input("pilih halaman : ")
        url = ("https://www.insecam.org/en/bycountry/ID/?page="+str(page))
        print ""
        res = requests.get(url, headers=headers)
        findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
        count = 1
        for _ in findip:
             hasil = findip[count]
             print ("{}({} {}{} {})").format(g,w,r,hasil,g)
             count += 1
     except:
        print ""
        print g+"Copy URL nya, buka pake apk puffin"+w
