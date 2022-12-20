# Method to set headers attributes that change per request (e.g. referer url, domain, etc...)
def get_headers(url):
    return {
        "referer": url.split("catalogue")[0],
        ":path": url.split(".com")[1]
    }
