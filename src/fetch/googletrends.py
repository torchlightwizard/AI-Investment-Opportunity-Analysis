from pytrends.request import TrendReq
import time

"""
    Blocks request due to no browser headers, user session cookies and other bot detection methods.
    Possible fix:
        https://stackoverflow.com/questions/50571317/pytrends-the-request-failed-google-returned-a-response-with-code-429
        Basically create a session manually while logged in, copy the real requests with session tokens.
        Extract their headers. Copy the headers and override them into your TrendReq's _get_data method

        However, since it requires continuous monitoring and interference due to session updating. It is not a permanent fix.
"""

company_names = ["deepseek"]

pytrends = TrendReq(hl='en-US', tz=360,  retries=5, backoff_factor=1.0)
pytrends.build_payload(company_names, cat=0, timeframe='today 1-m', gprop='news')
time.sleep(5)
df = pytrends.interest_over_time()
print(df)



# pytrends.interest_by_region (resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
# pytrends.related_topics ()
# pytrends.related_queries ()