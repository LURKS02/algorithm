import urllib.request
import json
import os
import argparse

DEFAULT_BASE_URL = "https://picsum.photos/v2/list"
DEFAULT_PAGE_SIZE = 100

def fetch_image_data(total_images):
    all_data = []
    for page in range((total_images // DEFAULT_PAGE_SIZE) + 1):
        params = f"?page={page}&limit={DEFAULT_PAGE_SIZE}"
        url = DEFAULT_BASE_URL + params
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())
                all_data.extend(data)
        except Exception as e:
            print(f"page fetching error at {page + 1}: {e}")
        if len(all_data) >= total_images:
            break
    return all_data[:total_images]

def download_images(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for item in data:
        image_url = item["download_url"]
        image_id = item["id"]
        ext = "png"
        file_path = os.path.join(output_dir, f"{image_id}.{ext}")
        try:
            with urllib.request.urlopen(image_url) as response:
                with open(file_path, "wb") as f:
                    f.write(response.read())
        except Exception as e:
            print(f"downloading error {image_url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download and save images.")
    parser.add_argument("--total", type=int, required=True, help="Total number of images to download.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the images.")
    args = parser.parse_args()

    data = fetch_image_data(args.total)
    download_images(data, args.output_dir)

if __name__ == "__main__":
    main()
