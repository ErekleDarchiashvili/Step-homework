import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://jsonplaceholder.typicode.com/photos/"

def get_photo(photo_id):
    response = requests.get(f"{BASE_URL}{photo_id}")
    return response.json()


def main():
    start_time = time.time()

    max_workers = 50

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        photos = list(executor.map(get_photo, range(1, 5001)))

    with open("photos.json", "w") as file:
        json.dump(photos, file, indent=4)

    end_time = time.time()

    print("Finished!")
    print(f"Total execution time: {end_time - start_time:.2f} seconds")




if __name__ == "__main__":
    main()