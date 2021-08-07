from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Korean Beauty
driver.get('https://www.ebay.com/itm/114862659651?hash=item1abe591843:g:QM0AAOSwfTdg0vwM')

sleep(1)

tree = html.fromstring(driver.page_source)

for product in tree.xpath('//div[contains(@id,"CenterPanelInternal")]'):
    title = product.xpath('.//h1[@class="it-ttl"]/text()')
    title_name = f'Nama Produk: {title}'

    price = product.xpath('.//span[@id="convbinPrice"]/text()')
    total_price = f'Harga Produk: {price}'
    
    img = driver.find_element_by_id("icImg").get_attribute("src")
    img_url = f'img_url: [{img}]'

    print(title_name, total_price, img_url)

driver.close()
     