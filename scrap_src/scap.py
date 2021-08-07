from selenium import webdriver
from lxml import html
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

for page_nb in range(0,21):
    driver.get('https://www.amazon.com/s?k=keyboard&page={}'.format(page_nb))

    sleep(1)

    tree = html.fromstring(driver.page_source)

    for product_tree in tree.xpath('//div[contains(@data-cel-widget, "search_result_")]'):
        title = product_tree.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()')
        price = product_tree.xpath('.//span[@class="a-offscreen"]/text()')
        img_url = product_tree.xpath('.//img[@class="s-image"]/text()')

        print(title, price, img_url)
    print("\n\n\n\n\n\n")

driver.close()
     