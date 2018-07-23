import requests
from bs4 import BeautifulSoup

def extract_meaning(word):
	request="http://dsalsrv02.uchicago.edu/cgi-bin/philologic/search3advanced?dbname=dasahindi&query="+word+"&searchdomain=headwords&matchtype=exact&display=utf8"
	html_content=requests.get(request).text
	soup=BeautifulSoup(html_content,"lxml")
	addresses=["http://dsalsrv02.uchicago.edu"+tag['href'] for tag in soup.find_all('a') if word in tag.get_text()]
	# print(addresses)
	meanings=[]
	for url in addresses:
		content=requests.get(url).text
		soup=BeautifulSoup(content,"lxml")
		meanings.append(soup.find('div2').get_text())
	return meanings

if __name__ == '__main__':
	word=input().strip()
	for i in extract_meaning(word):
		print(word+"-"+i)	