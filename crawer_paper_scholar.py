from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import json
import time
import os
import datetime
browsers = []
with open("browsers.jsonl", "r", encoding="utf-8") as file:
    browsers = [json.loads(line)['useragent'] for line in file]

# Khởi tạo WebDriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy ẩn nếu cần
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")
options.add_argument("user-agent=" + random.choice(browsers))
# options.add_argument("--force-device-scale-factor=0.75")
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920,1080)

driver.get("https://scholar.google.com/citations?view_op=list_works&hl=en&user=6bDvWw0AAAAJ&authuser=0&cstart=0&pagesize=100")
time.sleep(5)

# get all a elements with class name "gsc_a_at"
elements = [element.get_attribute("href") for element in driver.find_elements(By.CLASS_NAME, "gsc_a_at")]


for element in elements:
    driver.get(element)
    time.sleep(5)
    # Wait for the title element to be present
    title_paper = driver.find_element(By.ID, "gsc_oci_title").text
    url_paper = driver.find_element(By.CLASS_NAME, "gsc_oci_title_link").get_attribute("href")
    info = {}
    for x in driver.find_elements(By.CLASS_NAME, "gs_scl"):
        key = x.find_element(By.CLASS_NAME, "gsc_oci_field").text
        value = x.find_element(By.CLASS_NAME, "gsc_oci_value").text
        info[key] = value
    if len(info['Publication date'])==4:
        info['Publication date'] = info['Publication date']+"/01/01"
    if len(info['Publication date'])==7:
        info['Publication date'] = info['Publication date']+"/01"
    folder_name = datetime.datetime.strptime(info['Publication date'], '%Y/%m/%d').strftime('%Y-%m-%d') \
        +"_"+ title_paper.replace(" ", "_").replace("/", "_").replace("\\", "_").replace(":", "_").replace("?", "_").replace("*", "_").replace("<", "_").replace(">", "_").replace("|", "_")

    os.makedirs("content/publication", exist_ok=True)
    folder_name = os.path.join("content/publication", folder_name)
    # Check if the folder already exists
    if os.path.exists(folder_name+"/index.md"):
        print(f"File {folder_name}/index.md already exists. Skipping creation.")
        continue
    os.makedirs(folder_name, exist_ok=True)
    try:
        with open(folder_name+"/index.md", "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: '{title_paper}'\n")
            f.write("authors:\n")
            for author in info['Authors'].split(","):
                f.write(f"  - {author.strip()}\n")
            # f.write(f"publishDate: '{info['Publication date']}'\n")
            # convert publishDate to: '2023-01-14T00:00:00Z'
            f.write(f"publishDate: '{datetime.datetime.strptime(info['Publication date'], '%Y/%m/%d').strftime('%Y-%m-%dT%H:%M:%SZ')}'\n")
            # f.write(f"publishDate: '{info['Publication date'].replace('/', '-')}'\n")
            f.write(f"doi: ''\n")
            f.write("\n")
            f.write("# Schedule page publish date (NOT publication's date).\n")
            f.write(f"publication_types: [{'article-journal' if "Journal" in info else 'paper-conference'}]\n")
            f.write("\n")
            f.write("# Publication name and optional abbreviated publication name.\n")
            if "Journal" in info:
                f.write(f"publication: '{info['Journal']}'\n")
            if "Conference" in info:
                f.write(f"publication: '{info['Conference']}'\n")
            if "Book" in info:
                f.write(f"publication: '{info['Book']}'\n")
            f.write("\n")
            f.write(f"abstract: {info['Description'].replace(":"," ")}\n")
            f.write("\n")
            f.write("tags: []\n")
            f.write("\n")
            f.write("# Display this page in the Featured widget?\n")
            f.write("featured: true\n")
            f.write("\n")
            f.write("# Optional links to project, video, or paper slides\n")
            f.write(f"url_pdf: '{url_paper}'\n")
            f.write("url_code: ''\n")
            f.write("url_dataset: ''\n")
            f.write(f"url_poster: '{element}'\n")
            f.write("url_project: ''\n")
            f.write("url_slides: ''\n")
            f.write("url_source: ''\n")
            f.write("url_video: ''\n")
            f.write("\n")

            f.write("# Featured image\n")
            f.write("# To use, add an image named `featured.jpg/png` to your page's folder.\n")
            f.write("image:\n")
            f.write("  caption: ''\n")
            f.write("  focal_point: ''\n")
            f.write("  preview_only: false\n")
            f.write("\n")
            f.write("---\n")
            f.write("\n")

            f.write("|Field|Details|\n")
            f.write("|-----|-------|\n")
            for key, value in info.items():
                if key not in ["Publication date", "Authors", "DOI", "Conference", "Journal", "Description", "Total citations"]:
                    f.write(f"|{key}|{value.replace("\n"," - ")}|\n")
    except Exception as e:
        print(f"Error writing to file {folder_name}/index.md: {e}")
        # remove file index.md if error
        os.remove(folder_name+"/index.md")
        # remove folder if error
        os.rmdir(folder_name)