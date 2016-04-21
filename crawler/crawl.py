# -*- coding:utf-8 -*-
from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from HTMLParser import HTMLParser
from urllib import urlretrieve
from urlparse import urlparse, urljoin




# parse web and put urls to queue

class Parser(object,HTMLParser):
    def __init__(self, url, path):
        HTMLParser.__init__(self)
        self.url = url
        self.filename = self.cratefilename()
        self.path = path
        self.backurl = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for tempattr in attrs:
                if tempattr[0] == 'href':
                    self.backurl.append(tempattr[1])

    def gethtml(self, path):
        #print(self.path)
        with open(path, 'r') as f:
            return f.read()

    def downloadpage(self):
        #print(self.filename)
        try:
            pagehtml = urlretrieve(self.url, self.path+self.filename)
        except IOError:
            pagehtml = "***Error invaild URl '%s'" % self.url
        return pagehtml

    def cratefilename(self):
        name = self.url.split("/")[4].split(".")[0] + ".html"
       # print(name)
        return name

    def geturllist(self):
        return self.backurl

#控制整个抓取的逻辑

class crawler(object):
    def __init__(self, url, path):

        self.queue = []
        self.hascrawlurls = []
        self.faileurls = []
        self.path = path
        self.queue.append(url)

    def begin(self):

        tempurl = self.queue.pop()
        print("start crawl '%s'" % tempurl)
        parser = Parser(tempurl, self.path)
        rs = parser.downloadpage()
        print(rs)
        if rs[0] == "*":
            print("skip this page '%s'" % tempurl)
            return
        htmlfile = parser.gethtml(rs[0])
        parser.feed(htmlfile) #get links
        links = parser.geturllist()
        for link in links:
            if urlparse(link)[0] in ('http', 'https'):
                if link not in self.hascrawlurls:
                    self.queue.append(link)
        self.hascrawlurls.append(tempurl)
        print("success crawl '%s'" % tempurl)

    def startcrawl(self):
        while len(self.queue):
            self.begin()
        print("Success")

if __name__ == "__main__":
    path = "d:/pythonDairly/pythonDairlyExercise/crawler/data/"
    begainurl = "http://localhost:8080/Release/Log/logException.jsp"
    mycrawler = crawler(begainurl, path)
    mycrawler.startcrawl()

