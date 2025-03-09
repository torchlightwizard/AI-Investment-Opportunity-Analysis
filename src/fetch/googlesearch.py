from dotenv import load_dotenv as env
from datetime import datetime
import os
import requests

path_to_keys = "./keys/.env"
env(path_to_keys)

api_key = f"{os.getenv('GOOGLE_API_KEY')}"
cx = f"{os.getenv('GOOGLE_SEARCH_ENGINE_ID')}"



def get_response (url):
    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def get_company_results (search_query, days_offset=1, api_key=api_key, cx=cx):
    """
        Fetches the (1) time it took google to format a response, (2) how many searches were returned, (3) links to top 10 search results.

        Returns:
            List: [
                {
                    title,
                    link,
                    format_time,
                    search_results
                },
            ]
    """

    try:
        if not all(isinstance(arg, str) for arg in [api_key, cx, search_query]):
            raise TypeError("All Arguments must be strings.")

        month_year = datetime.now().strftime("%Y-%m").lower()
        search_query = f"+{search_query}%20after:{month_year}"

        url = f"https://customsearch.googleapis.com/customsearch/v1?q={search_query}&dateRestrict=d{days_offset}&key={api_key}&cx={cx}"
        res = get_response(url)
        items = res.get("items", [])
        data = []
        searchInformation = res.get("searchInformation", None)
        for item in items:
            data.append({
                "title": item.get("title", None),
                "link": item.get("link", None),
                "format_time": searchInformation.get("formattedSearchTime", None) if isinstance(searchInformation, dict) else None,
                "search_results": searchInformation.get("totalResults", None) if isinstance(searchInformation, dict) else None,
            })
        return data
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_company_results. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_company_results. Data error: {err}") # possible cause: wrong video id
    except Exception as err:
        print(f"Function: get_company_results. Unexpected error: {err}")
    return None