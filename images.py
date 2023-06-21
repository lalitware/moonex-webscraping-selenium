import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium webdriver (replace with the appropriate driver for your browser)
driver = webdriver.Chrome()

# Navigate to the webpage
# Replace with the URL of the webpage
driver.get("url")

# Find all the image elements
image_elements = driver.find_elements(By.XPATH, "//img[@src]")

# Extract the source attribute from each image element
image_urls = [image.get_attribute("src") for image in image_elements]

# Close the webdriver
driver.quit()


for image_url in image_urls:
    if 'category' in image_url:
        # Construct the complete URL of the image
        complete_url = image_url
        actual_image_name = complete_url.split('/')[-1]
        actual_image_name = actual_image_name.replace('%20', ' ')

        actual_lower_case_name = (actual_image_name.replace(' ', '-')).lower()
        removed_jpg_link = actual_lower_case_name[:-4]
        removed_jpg_link = removed_jpg_link.replace('.', '-')
        new_image_name = removed_jpg_link + ".jpg"

        link_file_address = "/var/www/html/moonex/image_name_file.txt"
        with open(link_file_address, mode='a') as my_new_file:
            my_new_file.write(actual_image_name + ":" + new_image_name + "\n")

        # Define the local file path to save the image
        file_path = "/var/www/html/moonex/category/" + \
            new_image_name  # Replace with your desired local file path

        # Set the User-Agent header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Create a custom request with headers
        request = urllib.request.Request(complete_url, headers=headers)

        # Download the image
        response = urllib.request.urlopen(request)

        # Save the image to a file
        with open(file_path, 'wb') as file:
            file.write(response.read())

        print("Image downloaded successfully!")
