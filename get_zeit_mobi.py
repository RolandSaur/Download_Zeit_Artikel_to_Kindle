from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import csv
import time
import subprocess

def get_pdf(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    boccat = soup.find("span","print-menu")
    link= boccat.find("a","print-menu__pdf")
    return link["href"]


with open('list_articles') as textfile:
	reader = csv.reader(textfile,delimiter=',')
	for row in reader:
		test_url=row[0]
		zeitlink=get_pdf(test_url)
		subprocess.call(["./download_zeit_pdf",zeitlink])
		
subprocess.call(["./convert_folder_mobi","/tmp/zeit"])
subprocess.call("./move_to_kindle")
subprocess.call(["./cleanup_tmp"])
    



