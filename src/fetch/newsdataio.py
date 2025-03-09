from dotenv import load_dotenv
import os
import requests
import time

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

api_key = f"{os.getenv('NEWS_DATA_IO_API_KEY')}"
limit = 10



def get_response (url):
    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def get_headlines (search_query, countries="cn,fr,de,in,us", categories="business,science,technology,world", days_offset=1, api_key=api_key, next_page=None, results_per_page=10):
    """
        Fetches news article ids, titles, and description. Parses the first page only.
        Unfortunately no content is available for free plans.
        
        Returns:
            Dict: {
                data: [
                    {
                        id,
                        source,
                        title,
                        description
                    },
                ],
                pages,
                next_page
            }
    """

    try:
        if not all(isinstance(arg, str) for arg in [api_key, search_query, countries, categories]):
            raise TypeError("All Arguments must be strings.")

        search_query = search_query.replace(" ", "%20")
        # hours = int(24 * days_offset)
        # if hours > 48:
        #     hours = 48
        if next_page is None:
            url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={search_query}&language=en&category={categories}&country={countries}"
        else:
            url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={search_query}&language=en&category={categories}&country={countries}&page={next_page}"
        res = get_response(url)
        if "results" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("results", [])
        data = []
        next_page = ""
        for item in items:
            data.append({
                "id": item.get("article_id", None),
                "source": item.get("source_name", None),
                "title": item.get("title", None),
                "description": item.get("description", None),
            })
        result = {
                "data": data,
                "pages": int(res.get("totalResults", 0)) / results_per_page,
                "next_page": res.get("nextPage", None)
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
                            id,
                            source,
                            title,
                            description
                        },
                    ],
                    pages,
                    next_page
                },
            ]
    """

    results = []
    try:
        max_pages = max_pages - 1
        result = get_headlines(search_query, countries, categories, days_offset)
        avbl_pages = result.get("pages", 0) - 1
        next_page = result.get("next_page", None)

        while (max_pages > 0) and (avbl_pages > 0):
            try:
                time.sleep(3)
                result = get_headlines(search_query, countries, categories, days_offset, next_page=next_page)
                next_page = result.get("next_page", None)
                results.append(result)
                avbl_pages = avbl_pages - 1
                max_pages = max_pages - 1
            except Exception as err:
                print(f"Function: get_headlines_next_page. Unexpected Error: {err}")
                print(f"Within while loop, on subsequent request.")
                return None
    except Exception as err:
        print(f"Function: get_headlines_next_page. Unexpected Error: {err}")
        print(f"On Initial Request.")
        return None
    return results