"""

    only a quick shot for playing around with the selenium modul

"""

# pip install selenium
# pip install bs4
# pip install chromedriver-autoinstaller

import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv



# options = Options()
# options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
website = os.getenv("EXAMPLE_REPORT_URL")
driver.get(website)
try:
    column_9 = WebDriverWait(driver, 100) \
        .until(EC.presence_of_element_located((By.CLASS_NAME, 'el-table_1_column_9')))
    table = WebDriverWait(driver, 100) \
        .until(EC.presence_of_element_located((By.CLASS_NAME, 'report-table')))
    # table_text = table.text
    # print (table_text)
    # if len(table_text) > 100:
    #     text_file = open("Output1.html", "w")
    #     text_file.write(table_text)
    #     text_file.close()
    html = driver.page_source
    if len(html) > 100:
        text_file = open("Output1.html", "w")
        text_file.write(html)
        text_file.close()
except Exception as ex:
    print (f"######\n{ex.with_traceback}")
finally:
    print (f"############  ")
    driver.quit()
