from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(executable_path="C:/Users/romanmisisin/Downloads/chromedriver_win32/chromedriver.exe"))
# driver = webdriver.Chrome("/Users/romanmisisin/Downloads/chrome-mac-arm64/Google\ Chrome\ for\ Testing.app")

format_link = lambda y, m, d: f"https://varta1.com.ua/archive/{y}-{m}-{d}/"

textes = []

def process_page_news_page(href: str):
    driver.get(href) 
    try :
        print('processing', href)
        # search for an main element
        main = driver.find_element(By.CSS_SELECTOR, "main")
        text = main.text
        driver.back()
        return text
    except:
        driver.back()
        return ""

def process_page_news():
    # search for a with href inside article with class "post"
    links = [a for a in driver.find_elements(By.CSS_SELECTOR, "div#categories article.post > a[href]")]
    print('links to process', [a.get_attribute("href") for a in links])
    for link in links:
        href = link.get_attribute("href")
        text = process_page_news_page(href)
        textes.append(text)

        

for year in [2022]:
    for month in [1, 2, 3, 4, 5, 6]:
        driver.get(format_link(year, month, 1))
        process_page_news()


display(textes)
driver.close()