import streamlit as st
import requests

# CSS styles
custom_css = """
<style>
body {
    background-color: #ffffff; /* Set background color to white */
    overflow: hidden; /* Hide overflow to prevent scrollbars */
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.square {
    width: 50px;
    height: 50px;
    background-color: #ff7f0e; /* Orange color for squares */
    animation: spin 3s linear infinite; /* Animation for spinning */
}

.hexagon {
    width: 50px;
    height: 50px;
    background-color: #6495ed; /* Cornflower blue color for hexagons */
    position: relative;
    top: 0;
    animation: moveUpDown 3s ease-in-out infinite alternate; /* Animation for moving up and down */
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

@keyframes moveUpDown {
    0% {
        top: 0;
    }
    100% {
        top: 50px;
    }
}
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def scraper(api_key, cx, treatment, num_results):
    base_url = "https://www.googleapis.com/customsearch/v1"

    results_fetched = 0
    while results_fetched < num_results:
        params = {
            "q": f"{treatment}",
            "cx": cx,  # Custom Search Engine ID
            "key": api_key,
            "num": min(10, num_results - results_fetched),  # Adjust the number of results per request
            "start": results_fetched + 1,  # Start index of results for pagination
            "sort": "date:r:20150101:20231231",  # Date range (adjust as needed)
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            
            for item in data.get("items", []):
                title = item.get("title", "")
                link = item.get("link", "")
                snippet = item.get("snippet", "")

                st.write(f"{results_fetched+1}) Title: {title}\nLink: {link}\nSnippet: {snippet}\n")
                st.write("##################################################")
                results_fetched += 1

            if "queries" in data and "nextPage" in data["queries"]:
                next_page = data["queries"]["nextPage"][0]
                if "startIndex" in next_page:
                    results_fetched = int(next_page["startIndex"]) - 1
            else:
                break

        else:
            st.write(f"Failed to retrieve web links. Status code: {response.status_code}")
            break

st.title("Google Search Results Scraper")

API_KEY = "YOUR_API_KEY"
SEACH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"
treatment = st.text_input("Enter Treatment Name:")
location = st.text_input("Enter the location of interest:")
num_results = st.number_input("Enter the number of results you want:", min_value=1, value=10)

if st.button("Scrape"):
    st.write("---------------------------------------------")
    scraper(API_KEY, SEACH_ENGINE_ID, treatment + " " + location, num_results)

# Animated elements
st.write('<div class="container">', unsafe_allow_html=True)
st.write('<div class="square"></div>', unsafe_allow_html=True)
st.write('<div class="hexagon"></div>', unsafe_allow_html=True)
st.write('</div>', unsafe_allow_html=True)
