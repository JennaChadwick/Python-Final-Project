import urllib

link = "https://sjmulder.nl/en/textonly.html"
f = urllib.urlopen(link)
myfile = f.read()
print(myfile)
