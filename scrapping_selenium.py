from selenium import webdriver
import os
import time

page_url = 'https://www.gettyimages.com/photos/german-shepherd'


save_directory = 'new_data_directory'

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

driver = webdriver.Chrome()

driver.get(page_url)

time.sleep(5)

image_elements = driver.find_elements_by_css_selector('.search-content__gallery-assets img')
image_urls = [element.get_attribute('src') for element in image_elements]

for i, image_url in enumerate(image_urls[:20]):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(save_directory, f'image_{i + 1}.jpg'), 'wb') as file:
            file.write(response.content)
            print(f'Zapisano obraz {i + 1}/{len(image_urls)}')
    else:
        print(f'Błąd podczas pobierania obrazu {i + 1}')


driver.quit()
