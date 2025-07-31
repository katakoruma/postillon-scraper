import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.request import urlretrieve


# URL of the website to download images from
website_url = 'https://www.der-postillon.com/p/bilder-des-tages-beeindruckende-fotos.html'
#website_url = 'https://www.der-postillon.com/2024/02/bilder-des-tages-februar-2024.html'
website_url = lambda year, month, month_written: f'https://www.der-postillon.com/{year}/{month:02}/bilder-des-tages-{month_written}-{year}.html'

year_list = [2024]
month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
month_written_list = ['januar','februar','marz','april','mai','juni','juli','august','september','oktober','november','dezember']

# Directory to save the images
#save_directory = 'Python_encrypted/postillon_newsticker_crawler/bild_des_tages/pictures'
save_directory = 'pictures'


def download_images(url, save_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Fetch webpage content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract image URLs
    img_urls = set()
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')

        if img_url and 'Bild-des-Tages' in img_url:
            img_urls.add(urljoin(url, img_url))

    # Download images
    for img_url in img_urls:
        try:
            # Get the filename from the URL
            img_filename = os.path.basename(urlparse(img_url).path)
            # Download the image
            urlretrieve(img_url, os.path.join(save_dir, img_filename))
            print(f"Downloaded: {img_filename}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

if __name__ == "__main__":

    for year in year_list:
        for month, month_written in zip(month_list, month_written_list):

            url = website_url(year, month, month_written)
            print(f"Downloading images from: {url}")
            download_images(url, save_directory)
