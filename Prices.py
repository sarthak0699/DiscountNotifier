import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL='https://www.amazon.in/Skybags-Stream-Polyester-Spacious-Backpack/dp/B07NKWW7JN/ref=sr_1_5?keywords=backpacks+skybag&qid=1573792368&s=luggage&sr=1-5'
headers={"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find(id="productTitle").get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    convert=price[2:len(price)]
    convert=float(convert.replace(',',''))
    if(convert < 1000):
        send_email()
def send_email():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sarthak0699@gmail.com','zmhnrabqnqmudwzl')
    subject = "Price Fell down"
    body= "Check link https://www.amazon.in/Skybags-Stream-Polyester-Spacious-Backpack/dp/B07NKWW7JN/ref=sr_1_5?keywords=backpacks+skybag&qid=1573792368&s=luggage&sr=1-5"
    msg= f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'sarthak0699@gmail.com','anshu1108.ab@gmail.com',f"Subject: {subject}\n\n{body}")
    print("Mail sent")
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)
