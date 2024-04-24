from selenium import webdriver
import os
import time

# Adres URL strony zawierającej obrazy
page_url = 'https://www.gettyimages.com/photos/german-shepherd'

# Katalog docelowy, gdzie zostaną zapisane obrazy
save_directory = 'new_data_directory'

# Sprawdź, czy katalog docelowy istnieje, jeśli nie, utwórz go
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Inicjalizacja sterownika przeglądarki Chrome
driver = webdriver.Chrome()

# Otwórz stronę
driver.get(page_url)

# Poczekaj chwilę, aby strona mogła się załadować
time.sleep(5)

# Pobierz adresy URL obrazów
image_elements = driver.find_elements_by_css_selector('.search-content__gallery-assets img')
image_urls = [element.get_attribute('src') for element in image_elements]

# Pobierz i zapisz obrazy
for i, image_url in enumerate(image_urls[:20]):  # Pobierz pierwsze 20 obrazów
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(save_directory, f'image_{i + 1}.jpg'), 'wb') as file:
            file.write(response.content)
            print(f'Zapisano obraz {i + 1}/{len(image_urls)}')
    else:
        print(f'Błąd podczas pobierania obrazu {i + 1}')

# Zamknij przeglądarkę
driver.quit()
