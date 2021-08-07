from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

for page_nb in range(0,200):
    driver.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=acer&_sacat={}'.format(page_nb))

    sleep(1)

    tree = html.fromstring(driver.page_source)

    for product_tree in tree.xpath('//div[contains(@id, "mainContent")]'):
        title = product_tree.xpath('.//h3[@class="s-item__title"]/text()')
        price = product_tree.xpath('.//span[@class="s-item__price"]/text()')
        
        img = driver.find_element_by_class_name("s-item__image-img").get_attribute("src")     
        img_url = f'[{img}]'

        print(title, price, img_url)
    print("\n\n\n\n\n\n") 

driver.close()
     