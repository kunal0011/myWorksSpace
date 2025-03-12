"""
LeetCode 535 - Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your 
encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL 
and the tiny URL can be decoded to the original URL.

Example:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Tiny URL: "http://tinyurl.com/4e9iAk"
Decoded: "https://leetcode.com/problems/design-tinyurl"

Note:
- Your implementation should support various URL formats
- The encoding should be deterministic or uniquely identifiable
- The decoding should always return the original URL
"""

import random
import string
import hashlib

class Codec:
    def __init__(self):
        """Initialize your data structure here."""
        self.url_to_code = {}
        self.code_to_url = {}
        self.chars = string.ascii_letters + string.digits
        self.base_url = "http://tinyurl.com/"
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
            
        # Generate a 6-character code using MD5 hash
        code = hashlib.md5(longUrl.encode()).hexdigest()[:6]
        
        # Handle potential collisions
        while code in self.code_to_url:
            code = ''.join(random.choice(self.chars) for _ in range(6))
            
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        return self.base_url + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        code = shortUrl.replace(self.base_url, '')
        return self.code_to_url.get(code, '')


class CodecCounter:
    """Alternative implementation using an incrementing counter"""
    def __init__(self):
        self.urls = []
        self.url_to_id = {}
        self.base_url = "http://tinyurl.com/"
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL using an index-based approach."""
        if longUrl in self.url_to_id:
            return self.base_url + str(self.url_to_id[longUrl])
            
        self.urls.append(longUrl)
        self.url_to_id[longUrl] = len(self.urls) - 1
        return self.base_url + str(len(self.urls) - 1)
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        try:
            index = int(shortUrl.replace(self.base_url, ''))
            return self.urls[index] if 0 <= index < len(self.urls) else ''
        except (ValueError, IndexError):
            return ''


def test_url_codec():
    """Test function to verify both codec implementations"""
    # Test cases with various URL formats and special characters
    test_cases = [
        "https://leetcode.com/problems/design-tinyurl",
        "https://www.example.com/path?param1=value1&param2=value2",
        "http://localhost:8080/api/v1/users",
        "https://github.com/user/repo#section",
        "ftp://ftp.example.com/files/document.pdf",
        "https://example.com/path with spaces",
        "https://example.com/~username/",
        "https://example.com/page?q=special@#$%^&*()",
        "https://subdomain.example.co.uk/path",
        "https://example.com/" + "very_long_path" * 10
    ]
    
    # Test both implementations
    codecs = [
        ("Hash-based Codec", Codec()),
        ("Counter-based Codec", CodecCounter())
    ]
    
    for codec_name, codec in codecs:
        print(f"\nTesting {codec_name}:")
        print("=" * 50)
        
        for i, original_url in enumerate(test_cases, 1):
            # Encode URL
            tiny_url = codec.encode(original_url)
            # Decode URL
            decoded_url = codec.decode(tiny_url)
            
            # Verify encoding/decoding
            encoding_ok = tiny_url.startswith("http://tinyurl.com/")
            decoding_ok = decoded_url == original_url
            
            print(f"\nTest {i}:")
            print(f"Original URL: {original_url}")
            print(f"Tiny URL: {tiny_url}")
            print(f"Decoded URL: {decoded_url}")
            print(f"Encoding valid: {'✓' if encoding_ok else '✗'}")
            print(f"Decoding matches: {'✓' if decoding_ok else '✗'}")
            
            # Additional tests for the same URL
            second_tiny = codec.encode(original_url)
            consistency_ok = second_tiny == tiny_url
            print(f"Consistent encoding: {'✓' if consistency_ok else '✗'}")
            
        # Test invalid decoding
        invalid_result = codec.decode("http://tinyurl.com/invalid")
        print("\nInvalid URL Test:")
        print(f"Decode invalid URL: {'✓' if invalid_result == '' else '✗'}")


if __name__ == "__main__":
    test_url_codec()