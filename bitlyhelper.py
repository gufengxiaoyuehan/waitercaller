try:
    from urllib2 import urlopen
except ModuleNotFoundError as e:
    from urllib.request import urlopen
import json

TOKEN="aec4ead97c8a993c47813add7f9c2804904dfe21"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"

class BitlyHelper:
    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urlopen(url).read()
            jr = json.loads(response)
            return jr['data']['url']
        except Exception as e:
            print(e)