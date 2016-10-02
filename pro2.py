import re
import urllib
def imgdownload():
	imgurl=raw_input("enter the link\n")
	webpage=urllib.urlopen(imgurl).read()
	RESULT=re.findall(re.compile('<img[^>]*src="([^">]+)"',re.IGNORECASE),webpage)
	f=open("output.txt","w")
	for i in RESULT:
		f.write(imgurl+i+"\n")

imgdownload()