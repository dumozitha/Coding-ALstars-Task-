# Website Translation Scraper for Class Central Website
### Developer Trial Task - Copy ClassCentral Pages and Translate to Hindi

* Scrape pages one level deep using HT Track, your custom script, or another app.

* Use Google Translate to Translate the text inside the HTML to Hindi. The hindi will be hard-
coded into the page.

* Upload to a webserver.
* Make sure all the javascript/css/etc. is loading correctly.

This project is a website scraper that uses Selenium to translate a website and then download the translated files into HTML. The translated files are then updated with the correct links and saved to the local directory.

### Requirements
Python 3.x
msedge-selenium-tools
selenium
beautifulsoup4

Note : You will also need to download the msedgedriver.exe file for your system and ensure it is in your PATH.

## Files
### 1.setup.py
This file contains the options for the Microsoft Edge browser used by the scraper. It sets the language to Hindi, disables extensions and the GPU, and sets some experimental options to enable page translation.

### 2.driver.py
This file contains a function to create a Selenium driver with the options specified in setup.py.

### 3.scraper.py
This file contains the main code for the scraper. It uses the driver to navigate to a given URL, scrape the HTML, and then translate and save the pages into HTML files. It also has a function to scroll down the page to ensure all content is loaded.

### 4.main.py
This file is the main entry point for the project. It creates a directory to save the HTML files, calls the scraper function to scrape and translate the website, and then calls the update_links function to update the links in the main HTML file with the newly saved translated HTML file paths.

## Usage
1. Install the required packages by running pip install msedge-selenium-tools selenium beautifulsoup4.
2. Download the msedgedriver.exe file for your system and ensure it is in your PATH.
3. Run python main.py to start the scraper. The translated HTML files will be saved in the html directory and the main HTML file with updated links will be saved as index.html.
4. Upload the HTML files to your web server to view the translated website.

Note: You may need to modify the options in setup.py to suit your requirements, such as changing the language or experimental options.
