from bs4 import BeautifulSoup
import requests

def visit(new_url, cookie):
        print("try: " + new_url)
        response = requests.get(new_url,cookies=cookie)
        source = response.text
        soup = BeautifulSoup(source,'html.parser')
        if ('{' in response.text):
                print(response.text)
                exit(1)
        for s in soup.findAll('a') :
                href = s.get('href')
                if(href != None):
                        new_url = url + href
                        visit(new_url,response.cookies)


url = 'http://web.chal.csaw.io:5010'
cookie = {'solChain':'stuff'}
visit(url + '/stuff',cookie)
