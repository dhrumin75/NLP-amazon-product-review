from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
'(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


url = 'https://www.amazon.in/Test-Exclusive-603/dp/B07HG8SBDV/ref=sr_1_5?dchild=1&keywords=oneplus+7&qid=1593437690&sr=8-5'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, features="lxml")

title = soup.select('#productTitle')[0].get_text().strip()
price = soup.find('span',id ='priceblock_ourprice').get_text().strip()
print(title)
print(price)