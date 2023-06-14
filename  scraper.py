import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/History_of_Mexico'

#  The first function to get citations count
def get_citations_needed_count(url):
    page=requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup)
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    count = len(citations)
    return count


#  The 2nd one to create function to get citations needed report
def get_citations_needed_report(url):
    all_citations =[]
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    # p =>  paragraph
    p= soup.find_all('p')
    for p in p:
        if p.find('a', title='Wikipedia:Citation needed'):
            # To clean the P's
            p = p.text.strip().replace('[citation needed]','')
            all_citations.append(p)
    return all_citations        
if __name__ == '__main__':
    print(get_citations_needed_count(url))
    x = get_citations_needed_report(url)
    for i in x:
        print(i,"\n")
  