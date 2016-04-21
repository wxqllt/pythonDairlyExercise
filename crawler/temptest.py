# -*- coding:utf-8 -*-
from HTMLParser import HTMLParser
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO
from urlparse import urlparse


class myhtmlparser(HTMLParser):
    def __init__(self, path):
        HTMLParser.__init__(self)
        self.links = []
        self.path = path
        #print(self.links)

    def handle_starttag(self, tag, attrs):

        if tag == "a":
            for attr in attrs:
                if attr[0] == 'href':
                     self.links.append(attr[1])
                     #print(attr[1])

    def getbackurllist(self):
        return self.links

    def gethtml(self):
       with open(self.path, 'r') as f:
           return f.read()

if __name__ == "__main__":

    #url = """'<html><head><title>test</title><body><a id="123" href="http://www.163.com">链接到163</a></body></html>'"""



    parser = myhtmlparser("d:\index.html")
    content = parser.gethtml()
    parser.feed(content)
   # print(content)
    links = parser.getbackurllist()
    print(links)
    print(urlparse(links[1]))
