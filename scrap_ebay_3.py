from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Sneakers
driver.get('https://www.ebay.com/itm/313609181550?hash=item490490596e%3Ag%3AmF0AAOSw4nhg9jCz&LH_BIN=1&LH_ItemCondition=1000')

sleep(1)

tree = html.fromstring(driver.page_source)

for product in tree.xpath('//div[contains(@id,"CenterPanelInternal")]'):
    title = product.xpath('.//h1[@class="it-ttl"]/text()')
    title_name = f'Nama Produk: {title}'

    price = product.xpath('.//span[@id="convbinPrice"]/text()')
    total_price = f'Harga Produk: {price}'
 
    print(title_name, total_price)

driver.close()
     