from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests
import json
import time

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

api_key = f"{os.getenv('NEWS_DATA_IO_API_KEY')}"
output_folder_path = "./scrap/data/news/"

search_query = "ai artificial intelligence"
countries = "cn,fr,de,in,us"
categories = "business,science,technology,world"
limit = 10



def get_response (url):
    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def write_response (output_folder_path, file_name, data):
    os.makedirs(output_folder_path, exist_ok=True)
    time_stamp = datetime.now().strftime(('%Y_%m_%dT%H_%M_%S'))
    output_file_path = os.path.join(output_folder_path, f"{file_name}_{time_stamp}.json")
    with open(output_file_path, "w") as file:
        json.dump(data, file, indent=4)
    return data



def get_headlines (api_key, output_folder_path, search_query, countries, categories, next_page=None, results_per_page=10):
    """
        Fetches news article ids, titles, and description for res["items"] and saves to a JSON file.
        Unfortunately no content is available for free plans.
        
        Returns:
            Response Object: Article Results | {data: {title, description}, next_page: next_page}
    """

    try:
        if not all(isinstance(arg, str) for arg in [api_key, output_folder_path, search_query, countries, categories]):
            raise TypeError("All Arguments must be strings.")

        search_query = search_query.replace(" ", "%20")
        if next_page is None:
            url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={search_query}&language=en&category={categories}&country={countries}"
        else:
            url = f"https://newsdata.io/api/1/latest?apikey={api_key}&q={search_query}&language=en&category={categories}&country={countries}&page={next_page}"
        res = get_response(url)
        if "results" not in res or not res["results"]:
            raise ValueError("Invalid response. No items found.")
        items = res.get("results", [])
        data = []
        next_page = ""
        for item in items:
            data.append({
                "source": item.get("source_name", None),
                "title": item.get("title", None),
                "description": item.get("description", None),
            })
        file_name = f"news_data_io"

        result = {
                "data": write_response(output_folder_path, file_name, data),
                "pages": int(res.get("totalResults", 0)) / results_per_page,
                "next_page": res.get("nextPage", None)
            }
        return result
    
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Data error: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None



def get_headlines_next_page (api_key, output_folder_path, search_query, countries, categories, max_pages=3):
    try:
        max_pages = max_pages - 1
        result = get_headlines(api_key, output_folder_path, search_query, countries, categories)
        avbl_pages = result.get("pages", 0)
        next_page = result.get("next_page", None)

        while (max_pages > 0) and (avbl_pages > 0):
            try:
                max_pages = max_pages - 1
                avbl_pages = avbl_pages - 1

                time.sleep(3)
                result = get_headlines(api_key, output_folder_path, search_query, countries, categories, next_page)
                next_page = result.get("next_page", None)
            except Exception as e:
                print(f"Unexpected Error - Subsequent Request: {err}")
                break
    except Exception as err:
        print(f"Unexpected Error - Initial Request: {err}")



# print(get_headlines(api_key, output_folder_path, search_query, countries, categories))
# get_headlines_next_page(api_key, output_folder_path, search_query, countries, categories)