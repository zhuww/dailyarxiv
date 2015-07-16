#!/usr/bin/python
import urllib, urllib2, sys
#from html2plaintext import *
from bs4 import BeautifulSoup

full_url = sys.argv[1]
the_page = urllib2.urlopen(full_url).read()
soup = BeautifulSoup(the_page, 'html.parser')
text = soup.get_text()
text = text.encode('ascii', 'ignore')
text.replace('\n\n', '\n')
text.replace('\n\n', '\n')
f = open('new', 'w')
f.write(text)
f.close()
#text = html2plaintext(the_page, encoding='UTF-8')
#artifacts = re.compile('(^\[\d+\]).*\n', re.VERBOSE)
#text = artifacts.sub('', text)
#artifacts = re.compile('^\n', re.VERBOSE)
#text = artifacts.sub('', text)
#text = text.encode('ascii', 'ignore')
#print text
