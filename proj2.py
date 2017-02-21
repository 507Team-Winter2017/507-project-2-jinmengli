#proj2.py

import requests
from bs4 import BeautifulSoup
import re

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
url = "http://nytimes.com"
soup = BeautifulSoup(requests.get(url).text,"html.parser")
lst= soup.find_all(class_="story-heading")
for i in range(10):
	if i>=len(lst): #see if there is no 10 headings
		break
	if lst[i].a:
		print (lst[i].a.text.replace("\n", " " ).strip())
	#else:
		#print (lst[i].contents[0].text.strip())
#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
url = "https://www.michigandaily.com/"
soup2 = BeautifulSoup(requests.get(url).text,"html.parser")
try:
	tmp=soup2.find_all("ol")
	lst2=tmp[0].find_all("li")
	for item in lst2:
		print (item.get_text())
except:
	print ("No Most Read")

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
url = "http://newmantaylor.com/gallery.html"
soup3 = BeautifulSoup(requests.get(url).text,"html.parser")
lst3=soup3.find_all("img")
for pic in lst3:
	if "alt" in pic.attrs: #attributes lists
		print (pic.attrs["alt"])
	else:
		print ("No alternative text provided!")


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
base= "https://www.si.umich.edu"
soup4 = BeautifulSoup(requests.get(url,headers={'User-Agent': 'SI_CLASS'}).text,"html.parser")
n=1
while 1:
	lst4=soup4.find_all("a",text="Contact Details")
	for p in lst4:
		if p.get("href",None)!=None: #have contact details
			link=base+p.get("href",None)
			tmp=BeautifulSoup(requests.get(link,headers={'User-Agent': 'SI_CLASS'}).text,"html.parser")
			email=tmp.find_all("a",href=re.compile("mailto"))
			if len(email)!=0: #see if there is a email for the professor
				print ("{} {}".format(n,email[0].get_text()))
				n+=1
	nextpage=soup4.find_all("a",title="Go to next page")
	if len(nextpage)!=0: #see if there is next page
		soup4=BeautifulSoup(requests.get(base+nextpage[0].get("href",None),headers={'User-Agent': 'SI_CLASS'}).text,"html.parser")
	else:
		break	




