import csv
import requests
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_domain(domain):
    url = f"https://{domain}"
    try:
        start = time.time()
        response = requests.get(url, timeout=5)  
        response_time = round(time.time() - start, 3)  
    except Exception:
        response_time = "N/A"

    try:
        ip_address = socket.gethostbyname(domain)
    except Exception:
        ip_address = "N/A"

    return {"domain": domain, "response_time": response_time, "ip_address": ip_address}


def main():
    start_time = time.time()

    domains = []
    with open("domains.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                domains.append(row[0].strip())

    results = []

    max_workers = 50

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_domain = {executor.submit(check_domain, d): d for d in domains}

        for future in as_completed(future_to_domain):
            results.append(future.result())

    results.sort(key=lambda x: x["domain"])

    with open("result.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["domain", "response_time", "ip_address"])
        for r in results:
            writer.writerow([r["domain"], r["response_time"], r["ip_address"]])

    end_time = time.time()
    print(f"Finished! Total execution time: {end_time - start_time:.2f} seconds")





if __name__ == "__main__":
    main()