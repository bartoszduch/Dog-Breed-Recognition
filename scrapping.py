import requests
import os
from bs4 import BeautifulSoup


def download_images_from_page(url, save_directory, max_images=20):
    response = requests.get(url)
    if response.status_code==200:
        soup = BeautifulSoup(response.content, 'html.parser')
        image_tags = soup.find_all('img')
        image_urls = [tag['src'] for tag in image_tags if 'src' in tag.attrs][:max_images]

        for i, image_url in enumerate(image_urls):
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(os.path.join(save_directory, f'image_{i + 1}.jpg'), 'wb') as file:
                    file.write(response.content)
                    print(f'Zapisano obraz {i + 1}/{len(image_urls)}')
            else:
                print(f'Błąd podczas pobierania obrazu {i + 1}')
    else:
        print('Błąd podczas pobierania strony')


page_url = 'https://www.pexels.com/pl-pl/szukaj/owczarek%20niemiecki/'

save_directory = 'new_data_directory'

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

download_images_from_page(page_url, save_directory, max_images=20)
