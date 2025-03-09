from dotenv import load_dotenv
from datetime import timedelta, date
import os
import requests
import time

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

api_key = f"{os.getenv('MARKET_AUX_API_KEY')}"
limit = 10



def get_response (url):
    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def get_headlines_by_company (company, days_offset=1, api_key=api_key, next_page=None, results_per_page=3):
    """
        Fetches news articles, sentiment and sources based on a company's stock listed name. Parses the first page only.
        
        Returns:
            Dict: {
                data: [
                    {
                        id,
                        entity_name,
                        match_score,
                        sentiment_score,
                        source,
                        title,
                        description,
                        snippet
                    },
                ],
                pages,
                page
            }
    """

    try:
        if not all(isinstance(arg, str) for arg in [api_key, company]):
            raise TypeError("api_key, company arguments must be strings.")
        if (next_page is not None) and (not isinstance(next_page, int)):
            raise TypeError("next_page argument must be int.")
        # if not isinstance(results_per_page, int):
        #     raise TypeError("results_per_page argument must be int.")

        yesterday = (date.today() - timedelta(days=days_offset)).isoformat()
        if next_page is None:
            url = f"https://api.marketaux.com/v1/news/all?api_token={api_key}&language=en&symbols={company}&published_after={yesterday}&sort=published_on&sort_order=desc&filter_entities=true"
        else:
            url = f"https://api.marketaux.com/v1/news/all?api_token={api_key}&language=en&symbols={company}&published_after={yesterday}&sort=published_on&sort_order=desc&filter_entities=true&page={next_page}"
        res = get_response(url)
        if "data" not in res:
            raise ValueError("Invalid response. No 'data' property found.")
        items = res.get("data", [])
        data = []
        next_page = ""
        for item in items:
            entities = item.get("entities", [])
            for entity in entities:
                data.append({
                    "id": item.get("uuid", None),
                    "entity_name": entity.get("name", None),
                    "match_score": entity.get("match_score", 0),
                    "sentiment_score": entity.get("sentiment_score", 0),
                    "source": item.get("source", None),
                    "title": item.get("title", None),
                    "description": item.get("description", None),
                    "snippet": item.get("snippet", None),
                })
        meta = res.get("meta", None)
        found = meta.get("found", 0) if isinstance(meta, dict) else 0
        page = meta.get("page", 1) if isinstance(meta, dict) else 1
        result = {
                "data": data,
                "pages": int(found) / results_per_page,
                "page": int(page)
            }
        return result

    except requests.exceptions.RequestException as err:
        print(f"Function: get_headlines_by_company. Request Error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_headlines_by_company. Value Error: {err}")
    except Exception as err:
        print(f"Function: get_headlines_by_company. Unexpected Error: {err}")
    return None



def get_headlines_by_search (search_query, days_offset=1, api_key=api_key, sentiment=[0.8, 0.5], next_page=None, results_per_page=3):
    """
        Fetches news articles, sentiment and sources based on a search. Parses the first page only.
        
        Returns:
            Dict: {
                data: [
                    {
                        id,
                        entity_name,
                        match_score,
                        sentiment_score,
                        source,
                        title,
                        description,
                        snippet
                    },
                ],
                pages,
                page
            }
    """

    try:
        search_query = search_query.replace(" ", "%20")
        if not all(isinstance(arg, str) for arg in [api_key, search_query]):
            raise TypeError("api_key, search_query arguments must be strings.")
        if (next_page is not None) and (not isinstance(next_page, int)):
            raise TypeError("next_page argument must be int.")
        # if not isinstance(results_per_page, int):
        #     raise TypeError("results_per_page argument must be int.")

        yesterday = (date.today() - timedelta(days=days_offset)).isoformat()
        if next_page is None:
            url = f"https://api.marketaux.com/v1/news/all?api_token={api_key}&language=en&search={search_query}&published_after={yesterday}&sort=published_on&sort_order=desc&sentiment_lte={sentiment[0]}&sentiment_gte={sentiment[1]}"
        else:
            url = f"https://api.marketaux.com/v1/news/all?api_token={api_key}&language=en&search={search_query}&published_after={yesterday}&sort=published_on&sort_order=desc&sentiment_lte={sentiment[0]}&sentiment_gte={sentiment[1]}&page={next_page}"
        res = get_response(url)
        if "data" not in res:
            raise ValueError("Invalid response. No 'data' property found.")
        items = res.get("data", [])
        data = []
        next_page = ""
        for item in items:
            entities = item.get("entities", [])
            for entity in entities:
                data.append({
                    "id": item.get("uuid", None),
                    "entity_name": entity.get("name", None),
                    "match_score": entity.get("match_score", 0),
                    "sentiment_score": entity.get("sentiment_score", 0),
                    "source": item.get("source", None),
                    "title": item.get("title", None),
                    "description": item.get("description", None),
                    "snippet": item.get("snippet", None),
                })
        meta = res.get("meta", None)
        found = meta.get("found", 0) if isinstance(meta, dict) else 0
        page = meta.get("page", 1) if isinstance(meta, dict) else 1
        result = {
                "data": data,
                "pages": int(found) / results_per_page,
                "page": int(page)
            }
        return result
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_headlines_by_search. Request Error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_headlines_by_search. Value Error: {err}")
    except Exception as err:
        print(f"Function: get_headlines_by_search. Unexpected Error: {err}")
    return None



def get_headlines_by_company_next_page (company, days_offset=1, api_key=api_key, max_pages=3):
    """
        Fetches news articles, sentiment and sources based on a company's stock listed name. Parses the first page, then parses next, until max_pages reached.
        
        Returns:
            List: [
                {
                    data: [
                        {
                            id,
                            entity_name,
                            match_score,
                            sentiment_score,
                            source,
                            title,
                            description,
                            snippet
                        },
                    ],
                    pages,
                    page
                },
            ]
    """
        
    results = []
    try:
        result = get_headlines_by_company(company, days_offset)
        avbl_pages = result.get("pages", 0) - 1
        current_page = result.get("page", 1) + 1

        while (current_page < max_pages) and (avbl_pages > 0):
            try:
                time.sleep(3)
                result = get_headlines_by_company(company, days_offset, next_page=current_page)
                current_page = result.get("page", current_page)
                results.append(result)
                avbl_pages = avbl_pages - 1
                current_page = current_page + 1
            except Exception as err:
                print(f"Function: get_headlines_by_company_next_page. Unexpected Error: {err}")
                print(f"Within while loop, on subsequent request.")
                return None
    except Exception as err:
        print(f"Function: get_headlines_by_company_next_page. Unexpected Error: {err}")
        print(f"On Initial Request.")
        return None
    return results



def get_headlines_by_search_next_page (search_query, days_offset=1, api_key=api_key, max_pages=3):
    """
        Fetches news articles, sentiment and sources based on a search. Parses the first page, then parses next, until max_pages reached.
        
        Returns:
            List: [
                {
                    data: [
                        {
                            id,
                            entity_name,
                            match_score,
                            sentiment_score,
                            source,
                            title,
                            description,
                            snippet
                        },
                    ],
                    pages,
                    page
                },
            ]
    """

    results = []
    try:
        result = get_headlines_by_search(search_query, days_offset)
        avbl_pages = result.get("pages", 0) - 1
        current_page = result.get("page", 1) + 1

        while (current_page < max_pages) and (avbl_pages > 0):
            try:
                time.sleep(3)
                result = get_headlines_by_search(search_query, days_offset, next_page=current_page)
                current_page = result.get("page", current_page)
                results.append(result)
                avbl_pages = avbl_pages - 1
                current_page = current_page + 1
            except Exception as err:
                print(f"Function: get_headlines_by_search_next_page. Unexpected Error: {err}")
                print(f"Within while loop, on subsequent request.")
                return None
    except Exception as err:
        print(f"Function: get_headlines_by_search_next_page. Unexpected Error: {err}")
        print(f"On Initial Request.")
        return None
    return results