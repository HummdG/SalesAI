import requests

def get_news_articles(api_key: str, cx: str, num_results: int, treatment: str):
    base_url = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": f"{treatment}",
        "cx": cx,  # Custom Search Engine ID
        "key": api_key,
        "num": num_results,  # Adjust the number of results per request
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
num_results = int(input("Enter the number of search results you want to generate permitted values (10 to 50):"))
print("---------------------------------------------")

if num_results > 100:
    raise ValueError("Cannot retrieve more than 100 search results")
else:
    for i in range(num_results//10):
        print(f"\n Results {(i*10)+1} to {(i*10)+1+9} \n")
        get_news_articles(API_KEY, SEACH_ENGINE_ID, 10, treatment)
    if num_results%10 != 0:
        print(f"\n Results{num_results-(num_results%10)+1} to {num_results} \n")
        get_news_articles(API_KEY, SEACH_ENGINE_ID, (num_results%10), treatment)