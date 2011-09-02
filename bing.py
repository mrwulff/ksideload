from urllib import *
from string import *
from shutil import *
import os


def sendtohtml(title,ur,b,bname):
    
    s=open("readinglist.html",'a')
    asin=split(ur,'/')
    asin=asin[5]
    asin=asin[:10]
    print asin
    s.write('<a href="')
    s.write( ur)
    s.write('" >')
    
    s.write(title)
    s.write("</a> <br>")
    try:
        os.mkdir('../copytokindle')
    except:
        'nothing'
    copy(bname,'../copytokindle/'+asin+'_EBSP.amz')

       

def googapi(b,bname): #lol google

    bing='946F1E3B6A7714BF5CEC341F123952303205B187'
    
    b=replace(b,'_',' ')
    
    
    a='http://api.search.live.net/xml.aspx?&sources=web&Appid='+bing+'&query=Kindle '+b
    

    "GOOOOOOOOOOOOOOOOOGLEING errrr binging"
    urlretrieve(a,'search.html')
    bing=open("search.html",'r')
    bing2=open("bing.html",'w')
    for line in bing.readlines():
        line=replace(line,'>','>\n')
        line=replace(line,'<','\n<')
        bing2.write(line)
    
    parsebing(b,bname)
    
    
    
    
def parsebing(b,bname):

    xml=open("bing.html",'r')
    flag=0
    i=0
    g=0
    for line in xml.readlines():
        i=i+1
        if 'dp/B00' in line:
            if flag==0:
                
                flag=1
                ur=line
                g=i-8
                
                #print i
    z=0
    xml.close()
    xml=open("bing.html",'r')
    
    for line in xml.readlines():
        z=z+1
        #print z
        if g==z:
            #print 'booya'
            title=line
            
    sendtohtml(title,ur,b,bname)
        
    


    
    

def finddir():
    format()
    try:
        os.chdir('ready')
    except:
        print '********************ERROR****************************'
        print "you need to have your books in a folder called 'ready'"
        print '********************ERROR****************************'

    a= os.getcwd()
    
    for files in os.walk(a):
        a= files[2]
    for a in range(len(files[2])):
        bname= files[2][a]
        if '.mobi' in bname:
            #print bname
            #print type(bname)
            #findbname(bname)
            'l'
    print "now open your ready/readinglist.html and click on each o those links and download the sample"
    print "after your kindle updated, copy your 'copytokindle' directory to the /.palmkindle on your touchpad"
    print "thanks to DCPeterson2000 on precentral.net and joesacher.com"
    os.system('open readinglist.html')
    



def findbname(bname):
    s=open(bname,'r')
    flag=0
    for line in s.readlines():
        if flag==0:
            flag=1
            a= line[:30]
            print a 
            googapi(a,bname)

                
def format():
    #print ""
    a=open("ready/readinglist.html",'w')
    a.write("<html>")
    a.write("<body>")
    a.write("This is all of your books that have free previews.  Click on the link to send to your kindle<br>")
    a.write("\n")
    a.close()

finddir()
