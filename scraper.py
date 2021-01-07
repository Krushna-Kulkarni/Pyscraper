import requests #obtain information from link
import time
import csv
from bs4 import BeautifulSoup 
#to parse that information. BeautifulSoup is a module used for scraping data. we can use selenium framework for extra functionality.
import scraper_mail
from datetime import date


today = str(date.today()) + ".csv"
csv_file = open(today, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Curent Price','Previous Close','Open','Bid','Ask','Day Range', '52-Week Range','Volume','Avg Volume'])


#look for website/Robots.txt to see which links are not allowed to scrape information from 

urls = ['https://in.finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch','https://in.finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch', 'https://in.finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch' 'https://in.finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch' ] #we can use multiple links using list, tuple or .txt file.
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'} #we are fetching the data multiple times so google may identify us as bot. To avoid this we are a our browser details using 'my user agent'.
#we are going to scrape data from the html page of link by their tags.(for eg. Title of page)

for url in urls:
    stock = [] #empt list to append tabl contents. for eg stock price, stock name etc.
    html_page = requests.get(url, headers) 

    #creating soup object for printing data. lxml is a parser. see documentation of BeatifulSoup
    '''About lxml, 
    It a basic parser that helps us to read and get content in HTML File. 
    (lxml provides a very simple and powerful API for parsing XML and HTML.)
    '''

    soup= BeautifulSoup(html_page.content, 'lxml') 

    '''for printing title of page'''
    # title = soup.find("title")

    # print(title.get_text())


    header_info =  soup.find_all("div",id="quote-header-info")[0] #here findall extracts all the tags so here by indexing we are extracting first element [0] common section having both title and current price of stock 
    stock_title = header_info.find("h1").get_text()  #here we extracting the stock title location by hierarchy of tags i.e. unique h1 tag (just like in html css code using inspect element)
    current_price = header_info.find("div", class_="D(ib) Mend(20px)").find("span").get_text() 
    #here we extracting the stock price using location by hierarchy of tags i.e. div and class and span of price  (just like in html css code using inspect element)
    stock.append(stock_title)
    stock.append(current_price)

    table_info = soup.find_all("div",class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")

    for i in range(0,8):
        heading_value = table_info[i].find_all("td")[1].get_text() #table content values
        stock.append(heading_value)
        
    csv_writer.writerow(stock)
    print("Stock Updated!")
    time.sleep(5)



csv_file.close()


scraper_mail.send(filename= today)