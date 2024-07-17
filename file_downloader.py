import requests
from tqdm import tqdm
import os

def download_file(url, folder="download"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Extract the file name from the URL
    file_name = os.path.join(folder, url.split("/")[-1])
    
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        with open(file_name, 'wb') as file, tqdm(
            desc=file_name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
    else:
        print(f"Failed to download {url}")

def download_files_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
        
    for url in urls:
        download_file(url)

if __name__ == "__main__":
    file_path = "urls.txt"  # Path to your .txt file with URLs
    download_files_from_file(file_path)
