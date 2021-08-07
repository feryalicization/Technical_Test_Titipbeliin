from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Laptop
driver.get('https://www.amazon.com/gp/product/B08XPQDC8D?pf_rd_r=RYXNH71AYG7C44NEYFRP&pf_rd_p=6fc81c8c-2a38-41c6-a68a-f78c79e7253f&pd_rd_r=18007918-202d-42e6-8ba2-770fdb8a343c&pd_rd_w=ILpjl&pd_rd_wg=2QCTP&ref_=pd_gw_unk')

sleep(1)

tree = html.fromstring(driver.page_source)

for product_center in tree.xpath('//div[contains(@class,"centerColAlign centerColAlign-bbcxoverride")]'):
    title = product_center.xpath('.//span[@class="a-size-large product-title-word-break"]/text()')
    title_name = f'Nama Produk: {title}'

    price = product_center.xpath('.//span[@class="a-size-medium a-color-price priceBlockBuyingPriceString"]/text()')
    total_price = f'Harga Produk: {price}'
 
    print(title_name, total_price)

driver.close()
     