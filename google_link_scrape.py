import requests

def get_news_articles(api_key, cx, treatment):
    base_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": f"{treatment}",
        "cx": cx,  # Custom Search Engine ID
        "key": api_key,
        "num": 10,  # Adjust the number of results per request
        "sort": "date:r:20150101:20231231",  # Date range (adjust as needed)
    }

    response = requests.get(base_url, params=params)
    # print(response.status_code)
    # print(response.text)

    if response.status_code == 200:
        data = response.json()
        
        for item in data.get("items", []):
            title = item.get("title", "")
            link = item.get("link", "")
            snippet = item.get("snippet", "")

            print(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n")
            print("##################################################")

    else:
        print(f"Failed to retrieve news articles. Status code: {response.status_code}")

API_KEY = "AIzaSyCjOxGey7Xlb_kaNp67TvPxS-t78XymXNI"
SEACH_ENGINE_ID = "33d3c2b2a85ff4505"
treatment = input("Treatment Name: ")
print("---------------------------------------------")
get_news_articles(API_KEY, SEACH_ENGINE_ID, treatment)