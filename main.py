# for scraping a web page to find downlaodable links of pdf files

# modules we're using (you'll need to download lxml)
import lxml.html, urllib
import urllib.request
from urllib.parse import urlparse
from urllib.parse import urljoin
import requests
import os
pdf_links=[]

# the url of the page you want to scrape
base_url = 'http://www.imperialctc.org/about-lta/financial-reports/'

# fetch the page
res = urllib.request.urlopen(base_url)

# parse the response into an xml tree
tree = lxml.html.fromstring(res.read())
print(tree)

# construct a namespace dictionary to pass to the xpath() call
# this lets us use regular expressions in the xpath
ns = {'re': 'http://exslt.org/regular-expressions'}

# iterate over all <a> tags whose href ends in ".pdf" (case-insensitive)
for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):
    
    pdf_links.append(urljoin(base_url, node.attrib['href']))


    
def pdf_file_download(pdf_links): 
    
        path = "/Users/pdfDowload/"

        # define the access rights
        access_rights = 0o755
        try:  
            os.mkdir(path, access_rights)
        except OSError:  
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s" % path)

        for link in pdf_links: 

            '''iterate through all links in video_links 
            and download them one by one'''

            # obtain filename by splitting url and getting  
            # last string 
            file_name = link.split('/')[-1]    

            print ("Downloading file:%s"%file_name )

            # create response object 
            r = requests.get(link, stream = True) 

            # download started 
            with open(path+file_name, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk) 

            print ("%s downloaded!\n"%file_name)

        print ("All pdf files downloaded!")
        return
print(pdf_links)
# download all videos 
pdf_file_download(pdf_links) 
