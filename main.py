from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.greaterkashmir.com/")
soup = BeautifulSoup(page.content, 'html.parser')

lis=[]
def h1_tags():
    for i in range(len(soup.find_all('h1'))):

        s=str(soup.find_all('h1')[i])
        len_title1=s.find('title=\"')+6
        title=s[len_title1:]
        len_link1=s.find('https://')
        len_link2=s.find("rel")    
        current_post_link=s[len_link1:len_link2-3]
        if soup.find_all('h1')[i].get_text() not in lis and current_post_link!=" ":
            lis.append(soup.find_all('h1')[i].get_text())
        if current_post_link not in lis: 
            lis.append(current_post_link)
            lis.append("")   
            

def h2_tags():
    for i in range(len(soup.find_all('h2'))):

        s=str(soup.find_all('h2')[i])
        len_title1=s.find('title=\"')+6
        title=s[len_title1:]
        len_link1=s.find('https://')
        len_link2=s.find("rel")    
        current_post_link=s[len_link1:len_link2-3]
        if soup.find_all('h2')[i].get_text() :
            lis.append(soup.find_all('h2')[i].get_text())
        if current_post_link not in lis or current_post_link =="" : 
            lis.append(current_post_link)
            lis.append("")   
h1_tags()
h2_tags()
for news in lis:
    print(news)
