# main.py
from scraper import scrape
from setup import update_links
import os

if __name__ == '__main__':

    url = "https://www.classcentral.com/"
    output_dir = 'output'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Step 1: Scrape the website and save the HTML files
    html_dir = os.path.join(output_dir, 'html')
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)
    #scrape(url, html_dir)


    # Step 2: Update the links in the main HTML file to point to the translated HTML files
  
    main_file_path = f"{html_dir}/Page{0}.html"
    target_file_path = f"{output_dir}/index.html"

    update_links(main_file_path ,target_file_path , html_dir )
    print(html_dir)
