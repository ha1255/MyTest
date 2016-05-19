# -*- coding: utf-8 -*-
#parse html with HTMLParser
import urllib
import os
import re
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):        
        HTMLParser.__init__(self)
        self.currentlink =""
        self.flag = False
        
        self.links =[]
        self.pictures =[]
        
        self.links_dict={}
        self.pictures_dict = {}
    
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            if len(attrs) == 0:
                pass
            else:
                for(variable,value) in attrs:
                    if variable == 'href':
                        #print variable +"\t" + value
                        self.links.append(value)
                        self.links_dict[value] = variable
        if tag == 'img':
            if len(attrs) == 0:
                pass
            else:
                for(variable,value) in attrs:
                    if variable == "src":
                        #print variable +"\t" + value
                        self.pictures.append(value)
                        self.pictures_dict[value] = variable
                        os
    def handle_data(self,data):
        pass
        #print data
        
    def handle_endtag(self, tag):
        pass
        #print "</%s>" % tag
    
def getHTMLSource(url):    
    resp = urllib.urlopen(url)
    st = resp.read()
    resp.close()
    return st

def downloadImage(imageUrl):  
    dir = "./pic"  
    try:  
        if not os.path.exists(dir):  
            os.mkdir(dir)  
    except:  
        print "Failed to create directory in %s"%dir  
        exit()  
    image = imageUrl.split('/')[-1]  
    path = dir+"/"+image  
    data = urllib.urlopen(imageUrl).read()  
    f = file(path,"wb")  
    f.write(data)
    f.close()
    print "download image success: " +imageUrl

def getBaiduSerachPictures(url):    
    resp = urllib.urlopen(url)
    ss = resp.read()   
    pattern = re.compile(r'"objURL":"(.*)"')    
    plist = pattern.findall(ss)
    i=0
    for p in plist:
        print p
        #downloadImage(p)
        i += 1

def getUrlLinks(url):
    a = MyHTMLParser()    
    st = getHTMLSource(url)
    a.feed(st)
    a.close()
    
    for l in a.links:
        print l
    print "======================================"
    
    with open("img.txt","w") as f:    
        for p in a.pictures:
            downloadImage(p)
            f.writelines(p+"\n")
            print "download image success: " +p

#test
url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=cover&pos=0#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1"
getBaiduSerachPictures(url)