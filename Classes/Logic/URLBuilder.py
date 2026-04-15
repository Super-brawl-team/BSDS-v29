from urllib.parse import quote, unquote,urlparse
class URLBuilder:
    
    def encode(URL:str) -> str:
        URLBuilder.isValidURL(URL)
        encoded = quote(URL, safe='')
        return f"brawlstars://extlink?page={encoded}"
    
    def decode(URL:str) -> str:
        prefix = "brawlstars://extlink?page="
        assert URL.startswith(prefix), "Not a valid Brawl Stars external link format"

        encoded = URL[len(prefix):]
        decoded = unquote(encoded)

        URLBuilder.isValidURL(decoded)
        return decoded
    
    def isValidURL(URL:str) ->str:
        parsed = urlparse(URL)
        assert parsed.scheme in ("http", "https"), f"Invalid scheme in URL: {URL}"
        assert parsed.netloc, f"No domain found in URL: {URL}"