# pip install selenium
# pip install chromedriver-autoinstaller

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def read_url_with_selenium(url, list_css_elements,file_output=None):
    """

    Reads an url with selenium
    Waits until some css classes are in the result
    Returns the generated html

    When a name of an output file is given, then stores the html in that file

    Example Call: read_html_with_selenium(
        'https://example.com/html_with_javascript.html',
        ['el-table_1_column_9','report-table'],
        file_output='Output.html')

    """

    WAIT_TIME = 100     # max wait time for getting the CSS classes in the html-code
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    try:
        wait = WebDriverWait(driver, WAIT_TIME)
        for css_element in list_css_elements:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, css_element)))
        time.sleep(1) # solves some timing problems
        html = driver.page_source
        if file_output:
            if len(html) > 100:
                text_file = open(file_output, "w")
                text_file.write(html)
                text_file.close()
    except Exception as ex:
        html = None
        print (f"######\n{ex.with_traceback}")
    finally:
        driver.quit()
    return html

if __name__ == "__main__":
    pass
