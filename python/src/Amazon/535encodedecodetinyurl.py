import random
import string


class Codec:
    def __init__(self):
        # Dictionary to store longUrl -> shortUrl and shortUrl -> longUrl mappings
        self.url_map = {}
        self.base_url = "http://tinyurl.com/"
        # Possible characters for short URL keys
        self.chars = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        # Generate a random short key and ensure it's unique
        short_key = ''.join(random.choices(self.chars, k=6))
        shortUrl = self.base_url + short_key

        # Store the mapping from shortUrl to longUrl
        self.url_map[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        # Return the longUrl that was mapped to the shortUrl
        return self.url_map.get(shortUrl, "")
