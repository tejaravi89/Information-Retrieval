#!/software/python/3.4/bin/python

# Minidom parser is used to get data from Reuters news artciles in XML form
from xml.dom import minidom
import os
os.chdir('/scratch1/rkandul/Reuters')  #path where XML file is present
print(os.getcwd())
fileCount = 0
files = filter(os.path.isfile, os.listdir( os.curdir ) ) 
for f in files:
 if f.endswith('.xml') and not f.endswith('.txt') and not f.endswith('build.xml'):
   
    opFile= open("/scratch1/rkandul/resultFolderMar25/result"+str(fileCount)+".txt", "a") 
    #Using above line, file like result1.txt or result2.txt or result100.txt is open place the parsed data
         
    fileCount +=1    
    if  not f.endswith('.txt'):
        opFile.write(f)
        opFile.write('\t')
    doc = minidom.parse(""+f)
    
    if     doc.getElementsByTagName("title").length !=0:
        title = doc.getElementsByTagName("title")[0]
        if not title.firstChild is None:
            opFile.write(title.firstChild.data)
        
    if     doc.getElementsByTagName("headline").length !=0:
        headline = doc.getElementsByTagName("headline")[0]
        if not headline.firstChild is None:
            opFile.write(headline.firstChild.data)

    if     doc.getElementsByTagName("byline").length !=0:
        byline = doc.getElementsByTagName("byline")[0]
        if not byline.firstChild.data is None:
            opFile.write(byline.firstChild.data)

    if     doc.getElementsByTagName("dateline").length !=0:
        dateline = doc.getElementsByTagName("dateline")[0]
        if not dateline.firstChild is None:
            opFile.write(dateline.firstChild.data)

        
    if     doc.getElementsByTagName("p").length !=0:
        texts = doc.getElementsByTagName("p")
        for p in texts:
            if not p.firstChild is None:
                opFile.write(p.firstChild.data)  
    opFile.close()

  
