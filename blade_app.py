import requests
import smtplib
import time
from bs4 import BeautifulSoup

url = 'LINK OF THE PRODUCT YOU WANT TO BUY'

headers = {'User-Agent':'YOUR USER AGENT CODE}

def check_price():
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id='product-name').get_text().strip()
    print(title)
    span = soup.find(id='offering-price')
    content = span.attrs.get('content')
    price = float(content)
    print(price)
    if(price < 700):
        send_mail(title)



def send_mail(title):
    sender = 'SENDER MAIL'
    receiver = 'RECEIVER MAIL'
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,'SENDER PASS')
        subject = title + ' the price you wanted has dropped!'
        body = 'You can go through this link => ' + url
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender,receiver,mailContent)
        print('Mail sended!')
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

while(1):
    check_price()
    time.sleep(60*60)
  
