import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium webdriver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.get("url")

links = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//p[@class='title']/a[@href]")))]

file_names = []
for link in links:

    actual_link = link.split('/')[-1]
    actual_link = actual_link.replace('%20', ' ')

    # To make the php link a lower case and hyphenated html link
    actual_lower_case_link = (actual_link.replace(' ', '-')).lower()
    removed_php_link = actual_lower_case_link[:-4]
    removed_php_link = removed_php_link.replace('.', '-')
    final_html_link = removed_php_link + ".html"
    file_address = "/var/www/html/moonex/" + final_html_link

    # To create a txt file of new and old links
    link_file_address = "/var/www/html/moonex/link_file.txt"
    with open(link_file_address, mode='a') as my_new_file:
        my_new_file.write(actual_link + ":" + final_html_link + "\n")

    # to get page source of the link and paste it to new file.
    driver.get(link)
    page_source = driver.page_source
    with open(file_address, mode='w') as my_new_file:
        my_new_file.write(page_source)

# To get all files in root diectory.
file_path = "/var/www/html/moonex/"
for folder, sub_folders, files in os.walk(file_path):
    if folder == file_path:
        files_list = files
        files_list.remove("link_file.txt")
        # print(files_list)

# To replace the old php links with new html links
with open(link_file_address, mode='r') as link_file:
    for line in link_file:
        link_list = line.split(':')
        php_link = link_list[0]
        html_link = link_list[1].strip()
        for file in files_list:
            with open(file_path + file, mode='r') as new_file:
                file_content = new_file.read()
            file_content = file_content.replace(php_link, html_link)

            with open(file_path + file, mode='w') as new_file:
                new_file.write(file_content)
