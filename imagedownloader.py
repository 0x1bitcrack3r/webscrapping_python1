import urllib
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
link="https://academics.vit.ac.in/student/view_photo_2.asp?rgno=13BIT000"
fname="0.jpeg"
d=list(link)
e=list(fname)
k=int(e[0])
n=int(d[65])
i=9
while i!=0:
	n=n+1
	d[66:]=str(n)
	link=''.join(d)
	k=k+1
	e[0:]=str(k)
	fname=''.join(e)
	urllib.urlretrieve(link,fname)
	i=i-1
d.remove('0')
i=99
while i!=0:
    n=n+1
    d[65:]=str(n)
    link=''.join(d)
    k=k+1
    e[0:]=str(k)
    fname=''.join(e)
    urllib.urlretrieve(link,fname)
    i=i-1
d.remove('0')
i=200
while i!=0:
    n=n+1
    d[64:]=str(n)
    link=''.join(d)
    k=k+1
    e[0:]=str(k)
    fname=''.join(e)
    urllib.urlretrieve(link,fname)
    i=i-1


