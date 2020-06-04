import requests
from bs4 import BeautifulSoup
import pprint

res=requests.get('https://news.ycombinator.com/news')
#print(res.text)

soup=BeautifulSoup(res.text,'html.parser')
#print(soup.find_all('div'))
links=soup.select('.storylink')
votes=soup.select('.score')

#print(votes[0])
#print(votes[0].get('id'))
def sorted_stories_by_votes(hnlist):
	return sorted(hnlist,key=lambda k:k['points'],reverse=True)

def create_custom_hn(links,votes):
	hn=[]
	for idx, item in enumerate(links):
		title=links[idx].getText()
		href=links[idx].get('href',None)
		points=int(votes[idx].getText().replace(' points',' '))
		if points>99:
			hn.append({'title':title,'link':href,'points':points})
	return sorted_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links,votes))

