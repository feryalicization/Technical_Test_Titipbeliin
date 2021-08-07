from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Handsfree
driver.get('https://www.amazon.com/Logitech-Wireless-Computer-Unifying-Receiver/dp/B087Z5WDJ2/ref=sr_1_24?dchild=1&fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=S6SM7661YSNJ6K3Z3HBZ&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1628341685&rnid=16225007011&s=computers-intl-ship&sr=1-24')

sleep(1)

tree = html.fromstring(driver.page_source)

for product_center in tree.xpath('//div[contains(@class,"centerColAlign centerColAlign-bbcxoverride")]'):
    title = product_center.xpath('.//span[@class="a-size-large product-title-word-break"]/text()')
    title_name = f'Nama Produk: {title}'

    price = product_center.xpath('.//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]/text()')
    total_price = f'Harga Produk: {price}'
 
    print(title_name, total_price)

driver.close()
     