from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Handsfree
driver.get('https://www.amazon.com/dp/B08RRZ2F57/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08RRZ2F57&pd_rd_w=6AmAq&pf_rd_p=887084a2-5c34-4113-a4f8-b7947847c308&pd_rd_wg=FhDHw&pf_rd_r=7CG8RA5YERENC11XKBW3&pd_rd_r=0bc7a2f4-dbfe-4f09-abfa-69bdfed95524&smid=A1H9MUIHI97NSU&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFLTjNGWlM1UTQxUjYmZW5jcnlwdGVkSWQ9QTA3ODg5NTExWE5YQjFKN1AyV08zJmVuY3J5cHRlZEFkSWQ9QTA5NzM4NzNOSzdRUjNFRTVKQlEmd2lkZ2V0TmFtZT1zcF9kZXRhaWwmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')

sleep(1)

tree = html.fromstring(driver.page_source)

for product_center in tree.xpath('//div[contains(@id,"ppd")]'):
    title = product_center.xpath('.//span[@class="a-size-large product-title-word-break"]/text()')
    title_name = f'Nama Produk: {title}'

    price = product_center.xpath('.//span[@class="a-size-medium a-color-price priceBlockSalePriceString"]/text()')
    total_price = f'Harga Produk: {price}'
 
    img = driver.find_element_by_id("landingImage").get_attribute("src")
    img_url = f'img_url: [{img}]'

    print(title_name, total_price, img_url)

driver.close()
     