import requests
from bs4 import BeautifulSoup

def get_google_links(query, num_links=100):
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    links = []
    start = 0

    while len(links) < num_links:
        params = {"q": query, "start": start}
        response = requests.get(base_url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.find_all("a")
        found_links = [a.get("href") for a in search_results if "href" in a.attrs]

        for link in found_links:
            if link.startswith("/url?q="):
                link = link.split("/url?q=")[1].split("&")[0]
                links.append(link)
                if len(links) >= num_links:
                    break

        start += 10

    return links[:num_links]

if __name__ == "__main__":
    query = "emsculpt clinics"
    links = get_google_links(query, num_links=100)
    for i, link in enumerate(links, start=1):
        print(f"{i}. {link}")