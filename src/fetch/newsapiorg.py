from dotenv import load_dotenv
from datetime import timedelta, date
import os
import requests
import time

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

api_key = f"{os.getenv('NEWS_API_ORG_API_KEY')}"
limit = 10



def get_response (url):
    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def get_headlines (search_query, countries="cn,fr,de,in,us", categories="business,science,technology,world", days_offset=1, api_key=api_key, next_page=None, results_per_page=100):
    """
        Fetches news article ids, titles, and description. Parses the first page only.
        Unfortunately no content is available for free plans.
        
        Returns:
            Dict: {
                data: [
                    {
                        source,
                        title,
                        description
                    },
                ],
                pages
            }
    """

    try:
        search_query = search_query.replace(" ", "%20")
        if not all(isinstance(arg, str) for arg in [api_key, search_query, countries, categories]):
            raise TypeError("All Arguments must be strings.")

        search_query = search_query.replace(" ", "%20")
        yesterday = (date.today() - timedelta(days=days_offset)).isoformat()
        if next_page is None:
            url = f"https://newsapi.org/v2/everything?apiKey={api_key}&language=en&from={yesterday}&q={search_query}"
        else:
            url = f"https://newsapi.org/v2/everything?apiKey={api_key}&language=en&from={yesterday}&q={search_query}&page={next_page}"
        res = get_response(url)
        if "articles" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("articles", [])
        data = []
        next_page = ""
        for item in items:
            source = item.get("source", None)
            data.append({
                "source": None if source is None else source.get("name"),
                "title": item.get("title", None),
                "description": item.get("description", None),
            })
        result = {
                "data":data,
                "pages": int(res.get("totalResults", 0)) / results_per_page
            }
        return result
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_headlines. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_headlines. Data error: {err}")
    except Exception as err:
        print(f"Function: get_headlines. Unexpected error: {err}")
    return None



def get_headlines_next_page (search_query, countries="cn,fr,de,in,us", categories="business,science,technology,world", days_offset=1, api_key=api_key, max_pages=3):
    """
        Fetches news article ids, titles, and description. Parses the first page, then parses next, until max_pages reached.
        Unfortunately no content is available for free plans.
        
        Returns:
            List: [
                {
                    data: [
                        {
                            source,
                            title,
                            description
                        },
                    ],
                    pages
                },
            ]
    """
        
    results = []
    try:
        current_page = 1
        result = get_headlines(search_query, countries, categories, days_offset)
        avbl_pages = result.get("pages", 0) - 1

        while (current_page < max_pages) and (avbl_pages > 0):
            try:

                time.sleep(3)
                result = get_headlines(search_query, countries, categories, days_offset, next_page=current_page)
                results.append(result)
                avbl_pages = avbl_pages - 1
                current_page = current_page + 1
            except Exception as err:
                print(f"Function: get_headlines_next_page. Unexpected Error: {err}")
                print(f"Within while loop, on subsequent request.")
                return None
    except Exception as err:
        print(f"Function: get_headlines_next_page. Unexpected Error: {err}")
        print(f"On Initial Request.")
        return None
    return results