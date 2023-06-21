import os

# To get all files in root diectory.
file_path = "/var/www/html/moonex/"
for folder, sub_folders, files in os.walk(file_path):
    if folder == file_path:
        files_list = files
        files_list.remove("image_name_file.txt")
        print(files_list)

# To replace the old php links with new html links
image_name_file_address = "/var/www/html/moonex/image_name_file.txt"
with open(image_name_file_address, mode='r') as link_file:
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
