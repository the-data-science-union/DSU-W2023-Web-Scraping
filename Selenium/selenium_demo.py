#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.by import By
#import requests
#import io
#from PIL import Image
#import time
##import names
#import pandas as pd
#
##PATH = "/Users/belle/Desktop/chromedriver"
#
#wd = webdriver.Chrome(ChromeDriverManager().install())
#
#def get_images_from_google(wd, delay, max_images):
## function to scroll down the webpage
#	def scroll_down(wd):
#		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#		time.sleep(delay)
## put the url of the google image search
#	url = "https://www.google.com/search?q=all+the+memes+in+world&tbm=isch&ved=2ahUKEwjNq82N4539AhXlNEQIHZJCBdcQ2-cCegQIABAA&oq=all+the+memes+in+world&gs_lcp=CgNpbWcQAzIGCAAQCBAeOgUIABCABDoGCAAQBRAeOgcIABCABBAYUABYhDVg8jhoCXAAeAaAAZsDiAH1LpIBCjYuNi4xMS41LjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=ZBbwY83pL-XpkPIPkoWVuA0&bih=658&biw=1305&rlz=1C5CHFA_enHK929HK930"
#
#    wd.get(url)
#
#	image_urls = set()
#	skips = 0
#
##scroll down and find html tags
#	while len(image_urls) + skips < max_images:
#		scroll_down(wd)
#		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
#
#		for img in thumbnails[len(image_urls) + skips:max_images]:
#			try:
#				img.click()
#				time.sleep(delay)
#			except:
#				continue
#
#			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
#
#			for image in images:
#				if image.get_attribute('src') in image_urls:
#					max_images += 1
#					skips += 1
#					break
#
#				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
#					image_urls.add(image.get_attribute('src'))
#					print(f"Found {len(image_urls)}")
#
#	return image_urls
#
## scrape the urls!
#urls = get_images_from_google(wd, 1, 10)
#print(urls)
## close the webdriver
#wd.quit()
#
#df2 = pd.DataFrame(urls)
#print(df2)
## export to csv and without index
#df2.to_csv('final_1.csv', index = False)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
#import names
import pandas as pd

PATH = "/Users/belle/Desktop/chromedriver"

wd = webdriver.Chrome(ChromeDriverManager().install())

def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = "https://www.google.com/search?q=all+the+memes+in+the+world+about+cats&tbm=isch&ved=2ahUKEwjxl5u76Z39AhVBhu4BHVpiChYQ2-cCegQIABAA&oq=all+the+memes+in+the+world+about+cats&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BAgAEB5Q8g1Ywhlg8RpoAHAAeACAAcECiAGuC5IBBzMuOC4wLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=Dx3wY7HUAsGMur8P2sSpsAE&bih=658&biw=1305&rlz=1C5CHFA_enHK929HK930"
    wd.get(url)

    image_urls = set()
    skips = 0

    while len(image_urls) + skips < max_images:
        scroll_down(wd)
        thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME, "n3VNCb")

            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(f"Found {len(image_urls)}")

    return image_urls

urls = get_images_from_google(wd, 1, 10)
print(urls)
wd.quit()

#random_name_set = {names.get_full_name() for i in range(50)}


df2 = pd.DataFrame(urls)

print(df2)
# export to csv and without index
df2.to_csv('final.csv', index = False)
