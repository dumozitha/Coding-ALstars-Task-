# scraper.py
import os
import codecs
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import get_driver

def scroll_down(driver, step_percent=0.08):
    """
    Scroll down to the bottom of the page to make sure all contents are translated.

    Args:
        driver: The Selenium WebDriver instance.
        step_percent: The percentage of the viewport height to scroll by.
            Default is 0.09 (9% of viewport height).

    Returns:
        None
    """
    # Get the height of the viewport
    viewport_height = driver.execute_script("return window.innerHeight")

    # Get the height of the document
    document_height = driver.execute_script("return document.body.scrollHeight")

    # Calculate the step size based on the document height and a percentage of the viewport height
    step_size = int((document_height * step_percent / viewport_height) * viewport_height)

    # Scroll down to the bottom of the page
    for j in range(0, document_height, step_size):
        driver.execute_script("window.scrollTo(0, "+str(j)+")")
        time.sleep(1)

    # Scroll to the top of the page
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME)
    time.sleep(1)

def get_links(driver, url):
    """
    Get all the links on the main page to scrap one level deep and return them as a list.

    Args:
        driver: The Selenium WebDriver instance.
        url: The URL of the page to get the links from.

    Returns:
        A list of links on the page.
    """
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete" and
            driver.find_element(By.TAG_NAME, "body") and EC.presence_of_element_located((By.CSS_SELECTOR, 'body.loaded')))
    time.sleep(15)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return links

def save_page_content(driver, url, path):
    """
    Save the HTML content of the given URL to the specified file path.

    Args:
        driver: The Selenium WebDriver instance.
        url: The URL of the page to save.
        path: The file path to save the page to.

    Returns:
        None
    """
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete" and
            driver.find_element(By.TAG_NAME, "body") and EC.presence_of_element_located((By.CSS_SELECTOR, 'body.loaded')))

    time.sleep(7)
    scroll_down(driver, step_percent=0.09)
    h = driver.page_source
    with open(path, "w", encoding="utf-8") as file:
        file.write(h)

def scrape(url, dir_path):
    """
    Scrape all pages linked one level deep to from the given URL and save their HTML content to files.

    Args:
        url: The URL to start scraping from.
        dir_path: The directory to save the HTML files in.

    Returns:
        None
    """
    driver = get_driver()
    links = get_links(driver, url)

    for i, link in enumerate(links):
        
        if link.startswith("/"):
            link = url + link
        link = link.replace("//", "/")

        path = os.path.join(dir_path, f"Page{i}.html")
        save_page_content(driver, link, path)

    driver.quit()
